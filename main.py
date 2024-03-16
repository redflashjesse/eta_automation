# importieren aller benötigtigten Funktionen aus den Dateinen
from unterprogramm import modul
import imports_and_variables

# Improts
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
import math

# gobal variables

# set dpi globally
plt.rcParams['savefig.dpi'] = 800
plt.rcParams["figure.figsize"] = (25, 10)

import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
import pickle  # For serializing data
import selenium  # For web automation
from selenium import webdriver  # For controlling web browser

def main():
    # Create a WebDriver
    driver = webdriver.Chrome()

    # Load the webpage
    driver.get('https://www.meineta.at/registered/boilers/status.xhtml?id=56602')

    # Find the input fields for username and password
    username = driver.find_element_by_id('loginForm:username')
    password = driver.find_element_by_id('loginForm:password')

    # Enter your login credentials
    username.send_keys('your_username')
    password.send_keys('your_password')

    # Click the login button
    login_button = driver.find_element_by_id('loginForm:login')
    login_button.click()

    # Wait for the webpage to load
    driver.implicitly_wait(10)

    # Get the HTML code of the webpage
    html = driver.page_source

    # Use bs4 to parse the HTML response and extract all data
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('div', class_='ui-panelgrid-cell')

    # Create a list to store the data
    data_list = []

    # Append each data entry to the list
    for item in data:
        data_list.append(item.text.strip())

    # Open a Pickle file in write mode and write the data into it
    with open('data.pickle', 'wb') as f:
        pickle.dump(data_list, f)

    # Close the file and the WebDriver
    f.close()
    driver.close()

if __name__ == "__main__":
    # Call main() function
    main()
