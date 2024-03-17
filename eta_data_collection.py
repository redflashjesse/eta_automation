import os
import time
from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

# grab secrets from file
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

DATA_CALL_INTERVAL = 60  # in seconds


def main():
    """
    # login to the website and navigate to the page with the heating system information, get the html content
    """
    # loop for collecting data
    loop_longtime_writing_pickle()


def navigate_to_scourse():
    # Create a WebDriver for Safari
    driver = webdriver.Firefox()

    # Load the login page
    driver.get('https://www.meineta.at/public/index.xhtml?faces-redirect=true')

    # Wait for the accept cookies button to be clickable and click it
    print('---accept cookies ---')
    accept_cookies_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Accept cookies') or contains(text(), 'Cookies erlauben')]"))
    )
    accept_cookies_button.click()
    time.sleep(1)

    # Find the login form elements
    print('---fetch logins ---')
    username_input = driver.find_element(By.ID, "txtUsername")
    password_input = driver.find_element(By.ID, "txtPassword")

    time.sleep(1)
    # Enter your credentials and click the login button
    print('---logging in---')

    username_input.send_keys(username)
    password_input.send_keys(password)

    # Wait for the login button to be clickable
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnLogin"))
    )
    # Click the login button
    login_button.click()

    # find and open Anlagenübersicht
    print('---opening anlagenübersicht---')
    anlagenuebersicht_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="pr-1" and text()="Anlagenübersicht"]'))
    )
    anlagenuebersicht_button.click()
    time.sleep(3)
    html_content = driver.page_source
    return html_content, driver


def extract_information(html_content):
    """
    Extract information from the HTML content
    """
    soup = BeautifulSoup(html_content, "html.parser")

    # find timestamp for this update call
    timestamp = soup.find("div", class_="text-muted small").text  # list-group-item d-flex justify-content-en")#.text
    # empty list to store the extracted information
    information_dict = {"Zeit": timestamp}

    # Find list items
    list_items = soup.find_all('li', class_='list-group-item')
    for li in list_items:
        # Finden Sie das d_flex-Element im aktuellen list_item
        d_flex = li.find('div', class_='d-flex')
        # Überprüfen Sie, ob d_flex vorhanden ist
        if d_flex:
            # Finden Sie flex_grow_1 und ml_1_text_right innerhalb von d_flex
            flex_grow_1 = d_flex.find('div', class_='flex-grow-1')
            ml_1_text_right = d_flex.find('div', class_='ml-1 text-right')

            # Überprüfen Sie, ob flex_grow_1 und ml_1_text_right vorhanden sind
            if flex_grow_1 and ml_1_text_right:
                # append to dict
                information_dict[flex_grow_1.get_text(strip=True)] = ml_1_text_right.get_text(strip=True)

    return information_dict, timestamp


def check_completeness(data, timestamp):
    """
    Check completeness of data in the information_list and fill missing values.
    TODO
    Args:
        data (list): List of dictionaries containing data to be checked.
        timestamp (str): Timestamp of the data.
    Returns:
        list: List of dictionaries with missing values filled or empty if more than three missing values.
    """
    # Liste der erwarteten Schlüssel
    expected_keys = [
        'Zeit', 'Kessel', 'Kessel Soll', 'Kesseldruck', 'Abgas',
        'Restsauerstoff', 'Abgasgebläse', 'Verbrauch seit Aschebox leeren',
        'Inhalt Pelletsbehälter', 'Kollektor', 'Ladezustand',
        'Angeforderte Leistung', 'Fühler 1 (oben)', 'Fühler 2', 'Fühler 3',
        'Fühler 4', 'Fühler 5', 'Vorlauf', 'Heizkurve', 'Vorrat',
        'Außentemperatur', 'Externe Störmeldung'
    ]

    complete_data = []

    # check for missing keys
    for entry in data:
        missing_keys = [key for key in expected_keys if key not in entry]
        if len(missing_keys) <= 3:
            # if 3 or less keys are missing, add it to the entry with value ''
            for key in missing_keys:
                entry[key] = ''
            complete_data.append(entry)
        else:
            # if more than 3 keys are missing, add an empty entry
            complete_data.append({'Zeit': timestamp, '': ''})
    print('--- data checked for completeness ---')
    return complete_data


def loop_longtime_writing_pickle():
    """"loop for collecting data every 15 minutes"""
    print('---starting loop for collecting data---')
    print(f'starttime: {datetime.now()}')

    while True:
        # Setzen Sie die Startzeit der Aufnahme
        start_time = datetime.now()
        print("---starting call---")
        html_content, driver = navigate_to_scourse()

        print("---extracting data---")
        information_dict, timestamp = extract_information(html_content)

        # todo later
        # print("---checking completeness---")
        # information_dict = check_completeness(information_dict, timestamp)
        print('---')
        # close the driver
        driver.close()
        # specify the dimestamp column as index

        df = pd.DataFrame([information_dict])
        df.set_index('Zeit', inplace=True)
        print(df.head())

        # check if a . csv already exists
        if os.path.exists('data.csv'):
            # append the data to the existing .csv
            df.to_csv('data.csv', mode='a', header=False)
        else:
            # save the data to a .csv
            df.to_csv('data.csv')

        # calc how long the call needed
        end_time = datetime.now()
        call_duration = end_time - start_time
        print(f"Der Aufruf dauerte {call_duration} Sekunden.")

        # waiting time for the next call of the website,
        print(f"---waiting for {DATA_CALL_INTERVAL} seconds---")
        time.sleep(DATA_CALL_INTERVAL - call_duration.total_seconds())


if __name__ == "__main__":
    main()
