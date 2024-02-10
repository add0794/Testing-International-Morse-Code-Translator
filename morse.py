from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    driver = webdriver.Chrome()  # You can use any other browser driver
    driver.get("https://morsedecoder.com/")


    # Find and access the Morse Alphabet
    driver.find_element(By.XPATH, "//*[@id='show-alphabet']/span[2]").click()

    time.sleep(2) # Take 2 seconds before accessing the tables

    # Get the three tables (i.e. letters, numbers, and punctuation) as a nested list

    # Morse letters

    letter_table = driver.find_element(By.CSS_SELECTOR, "#characters > div:nth-child(3) > table")
    letter_rows = letter_table.find_elements(By.TAG_NAME, "tr")

    letters_dict = {}

    for row in letter_rows:
        # Find all cells within the current row
        cells = row.find_elements(By.TAG_NAME, "td")
        # Ensure there are at least two cells in the row
        for i in range(0, len(cells) - 1, 2):
            # Extract the text from the first and second cells
            key = cells[i].text.strip()
            value = cells[i + 1].text.strip()
            letters_dict[key] = value


    # Morse numbers

    number_table = driver.find_element(By.CSS_SELECTOR, "#characters > div:nth-child(5) > table")
    number_rows = number_table.find_elements(By.TAG_NAME, "tr")

    numbers_dict = {}

    for row in number_rows:
        # Find all cells within the current row
        cells = row.find_elements(By.TAG_NAME, "td")
        # Ensure there are at least two cells in the row
        for i in range(0, len(cells) - 1, 2):
            # Extract the text from the first and second cells
            key = cells[i].text.strip()
            value = cells[i + 1].text.strip()
            numbers_dict[key] = value


    # Morse puncutation 

    punctuation_table = driver.find_element(By.CSS_SELECTOR, "#characters > div:nth-child(7) > table")
    punctuation_rows = punctuation_table.find_elements(By.TAG_NAME, "tr")

    punctuation_dict = {}

    for row in punctuation_rows:
        # Find all cells within the current row
        cells = row.find_elements(By.TAG_NAME, "td")
        # Ensure there are at least two cells in the row
        for i in range(0, len(cells) - 1, 2):
            # Extract the text from the first and second cells
            key = cells[i].text.strip()
            value = cells[i + 1].text.strip()
            punctuation_dict[key] = value


    # Nest the dictionaries in a list
    nested_list = [letters_dict, numbers_dict, punctuation_dict]


finally:
    # Quit the WebDriver session to close the browser
    driver.quit()