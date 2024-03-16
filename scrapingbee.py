from scrapingbee import ScrapingBeeClient

# Erstellen Sie einen ScrapingBeeClient
client = ScrapingBeeClient(api_key='YOUR-API-KEY')

# Definieren Sie die URL, die Sie besuchen möchten
data_url = 'https://example.com/data'

# Definieren Sie das JavaScript-Szenario, das das Login ausführt
js_scenario = {
    "instructions" : [
        {
            "fill": [
                "#username",
                "your_username"
            ]
        }, # Geben Sie den Benutzernamen ein
        {
            "fill": [
                "#password",
                "your_password"
            ]
        }, # Geben Sie das Passwort ein
        {
            "click": "#login"
        }, # Klicken Sie auf den Anmelden-Button
        {
            "wait": 1000
        } # Warten Sie eine Sekunde
    ]
}

# Senden Sie eine GET-Anfrage mit dem JavaScript-Szenario
response = client.get(data_url, params={
    "js_scenario": js_scenario
})

# Verarbeiten Sie die Antwort
print(response.text)
