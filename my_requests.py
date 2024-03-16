import requests

# Erstellen Sie eine Sitzung
s = requests.Session()

# Senden Sie eine POST-Anfrage an die Login-URL mit Ihren Anmeldedaten
login_url = 'https://example.com/login'
data = {
    'username': 'your_username',
    'password': 'your_password'
}
response = s.post(login_url, data)

# Überprüfen Sie den Statuscode und speichern Sie die Cookies
if response.status_code == 200:
    print('Login erfolgreich')
    cookies = response.cookies
else:
    print('Login fehlgeschlagen')
    exit()

# Senden Sie eine GET-Anfrage an die URL, die Sie besuchen möchten
data_url = 'https://example.com/data'
response = s.get(data_url, cookies=cookies)

# Verarbeiten Sie die Antwort
print(response.text)
