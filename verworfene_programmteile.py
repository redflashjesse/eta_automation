def extract_infos_screeshot(driver):
    """Extract information from a screenshot of the webpage using OCR (Optical Character Recognition) with Tesseract."""
    # set a break
    time.sleep(2)

    # Set the path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # Screenshot erstellen
    driver.save_screenshot('screenshot.png')

    # Screenshot in ein Pillow Image laden
    screenshot = Image.open('screenshot.png')

    # Texterkennung mit Pytesseract durchführen, to data oder direkt zu pandas.dataframe

    #erkannter_text_dict = pytesseract.image_to_data(screenshot, lang='deu', output_type=Output.DICT)

    erkannter_text = pytesseract.image_to_string(screenshot)
    zeilen = erkannter_text.strip().split('\n')
    datensatz = pd.DataFrame(zeilen, columns=['Text'])
    # Entfernen von leeren Zeilen
    zeilen = [zeile for zeile in zeilen if zeile.strip()]

    # Überprüfen Sie, ob der Text in Spalten unterteilt ist
    spalten = None
    for zeile in zeilen:
        if ':' in zeile:
            spalten = [teil.strip() for teil in zeile.split(':')]
            break

    # Wenn Text in Spalten unterteilt ist, erstellen Sie einen DataFrame
    if spalten:
        datensatz = pd.DataFrame([zeile.split(':') for zeile in zeilen], columns=spalten)
        print(datensatz)
    else:
        print("Der erkannte Text ist nicht in einer strukturierten Form.")


    print('erkannter_text:', erkannter_text)

    print('datensatz:', datensatz)

    erkannter_text_dataframe = pd.DataFrame([erkannter_text.split('\n')], columns=['Text'])
    print('erkannter_text_dataframe:', erkannter_text_dataframe)
    print('erkannter_text:', erkannter_text)

    #, output_type=Output.DATAFRAME) #dict values, data

    return erkannter_text


def sort_out_data(extractinfos_by_driver):
    '''Sort out the data from the OCR result'''
    data=extractinfos_by_driver
    # Split the text into lines
    lines = data.split('\n')

    # Remove empty lines and lines containing only whitespace
    lines = [line for line in lines if line.strip()]

    # Remove lines containing only numbers
    lines = [line for line in lines if not re.match(r'^\d+$', line)]

    return lines


def extract_heating_system_info(driver):
    try:
        # Locate the carousel items
        carousel_items = driver.find_elements(By.CLASS_NAME, "carousel-item")

        # Loop through each carousel item
        for item in carousel_items:
            # Check  if the item contains heating system information
            if "Kessel" in item.text:
                # Extract relevant information about the heating system
                system_name = item.find_element(By.CLASS_NAME, "h5").text
                disturbance = item.find_element(By.CLASS_NAME, "text-muted").text
                temperature_elements = item.find_elements(By.CLASS_NAME, "list-group-item")
                temperatures = {
                    element.find_element(By.CLASS_NAME, "flex-grow-1").text: element.find_element(By.CLASS_NAME,
                                                                                                  "").text for element
                    in temperature_elements}

                ''''# Print the extracted information
                print("Heating System:", system_name)
                print("Disturbance:", disturbance)
                print("Temperatures:")
                for key, value in temperatures.items():
                    print(f"{key}: {value}")
                print("\n")'''

    except Exception as e:
        print("Error:", e)