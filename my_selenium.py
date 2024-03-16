import selenium
from selenium import webdriver

# Erstellen Sie einen WebDriver
driver = webdriver.Chrome()

# Laden Sie die Webseite
driver.get('https://example.com/login')

# Finden Sie die Eingabefelder für Benutzername und Passwort
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')

# Geben Sie Ihre Anmeldedaten ein
username.send_keys('your_username')
password.send_keys('your_password')

# Klicken Sie auf den Anmelden-Button
login_button = driver.find_element_by_id('login')
login_button.click()

# Warten Sie, bis die Webseite geladen ist
driver.implicitly_wait(10)

# Laden Sie die URL, die Sie besuchen möchten
data_url = 'https://example.com/data'
driver.get(data_url)

# Verarbeiten Sie die Antwort
print(driver.page_source)

# Schließen Sie den WebDriver
driver.close()
