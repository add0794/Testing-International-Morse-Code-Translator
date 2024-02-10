import morse # User-developed module, which provides the Morse alphabet in a nested list
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time


"""
This module tests if two *English* Morse code messages match. 

The first is developed by using Selenium to get its alphabet entirely by scraping from this website: https://morsedecoder.com/. Using an input message as its output, the Morse code is created using the nested list from the Selenium-derived alphabet. The second is developed by sending that message to the Text input field from the aforementioned website and returning the output Morse code.

Learn more about Morse code here, as well as how it's applied in other languages: https://www.babbel.com/en/magazine/how-does-morse-code-work
"""


start_time = time.time() # Begin execution time

message = input("What would you like to say? ")

text_selector = "/html/body/main/div[2]/div[2]/div[1]/textarea" # Access the text input field
morse_selector = "/html/body/main/div[2]/div[2]/div[2]/textarea" # Access the Morse code input field

# Make the message accessible as a list to iterate over
list_message = [char for char in message.upper()]

# Initialize morse_message variable
morse_message = ""

# Iterate over each character in list_message
for letter in list_message:
    # Check if the character is a space
    if letter == ' ':
        # If the character is a space, append "/" to morse_message
        morse_message += "/ "
    else:
        # If the character is not a space, iterate over each dictionary in morse.nested_list
        for code_dict in morse.nested_list:
            # Check if the character is present in the current dictionary
            if letter in code_dict:
                # If the character is found, append its Morse code to morse_message
                morse_message += code_dict[letter] + " "

# Initialize morse_message variable
morse_message = ""

# Iterate over each character in the input message
for letter in message:
    # Check if the current character is a space
    if letter == ' ':
        morse_message += "/ "
    # Check if the current character is a newline
    elif letter == "\n":
        morse_message += "# "
    else:
        # Iterate over each dictionary in morse.nested_list
        for code_dict in morse.nested_list:
            # Check if the character is present in the current dictionary
            if letter.upper() in code_dict:
                # If the character is found, append its Morse code to morse_message
                morse_message += code_dict[letter.upper()] + " "


# Option #1: Keep the browser open 
# chrome_options = Options() 
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)  

# Option #2: Close the browser once done

try: 
    driver = webdriver.Chrome() # You can use any other browser driver
    driver.get("https://morsedecoder.com/")

    input_field = driver.find_element(By.XPATH, text_selector)

    # Send keys to the input field
    input_field.send_keys(message)

    # Add a delay to observe the entered text
    time.sleep(10)

    # Retrieve the text entered into the input field
    output_field = driver.find_element(By.XPATH, morse_selector)
    entered_text = output_field.get_attribute("value")

    # Check if the strings are a match.
    if entered_text.strip() == morse_message.strip():
        print("Test has passed.")
    else:
        print("Try again")

finally:
    # Quit the WebDriver session to close the browser
    driver.quit()


print("Result by using Selenium:", morse_message) # Print the Selenium-derived Morse code message
print("Result by using website:", entered_text) # Print the website-derived Morse code message
end_time = time.time() # End execution time
execution_time = (end_time - start_time) # Calculate the time it took to run this process
print(f"Process finished, and it took {execution_time} seconds.") # Print execution time