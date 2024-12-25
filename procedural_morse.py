from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1) Getting Morse alphabet from online

def morse_alphabet(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr')
    for row in rows:
        characters = soup.find_all('td')
        cols = [ele.text.strip() for ele in characters]
    english_letters = [code for code in cols[0::4]]
    morse_code = [code for code in cols[2::4]]
    df = pd.DataFrame({'English': english_letters, 'International Morse': morse_code})

    punctuation_marks = pd.DataFrame([
    ['.', '.-.-.-'],
    [',', '--..--'],
    ['?', '..--..'],
    ['!', '-.-.--'],
    ['(', '-.--.'],
    [')', '-.--.-'],
    ['\'', '.----.'],
    [';', '-.-.-.'],
    [':', '---.../'],
    ['"', '.-..-.'],
    ['-', '-....-'],
    ['/', '-..-.'],
    ['$', '...-..-'],
    [' ', '/'],
    ['&', '._...'],    
    ['@', '.__._.'],   
    ['=', '_..._'],    
    ['+', '._._.'],    
    ['_', '..__._'],
    ], columns=df.columns)  # Use the same column names as your existing df

    # Concatenate the DataFrames
    df = pd.concat([df, punctuation_marks], axis=0, ignore_index=True)

    # print(df)

    return df

morse = morse_alphabet('https://morsecodetranslator.com/american-morse-code-translator/')
# print(morse)

# 2) Inputting text to the International Morse Code translator (e.g. "Hi, I'm Alex.")

def bs4_morse_code(statement, url):
    text = statement
    # Alex
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        # time.sleep(30)

        # Locate the input field using its id
        word_input = driver.find_element(By.ID, 'input')
        # Input the word into the text area
        word_input.send_keys(text)

        # Retrieve the value from the same textarea
        word_output = driver.find_element(By.ID, 'output')
        # Output the Morse code from the text area
        morse_response = word_output.get_attribute("value")

        return morse_response
    except:
        print("An exception occurred")

# morse_response = bs4_morse_code('https://morsedecoder.com/')

# 3) Creating Morse code from the self-derived Morse alphabet

def self_derived_morse(statement, morse_alphabet):
    morse_code = []

    for char in statement:
        # Convert character to uppercase and check if it's in the DataFrame
        row = morse_alphabet[morse_alphabet['English'] == char.upper()]
        if not row.empty:
            # Append the corresponding Morse code
            morse_code.append(row['International Morse'].values[0])
        else:
            # Handle unknown characters
            morse_code.append("/")

    # Join Morse code with spaces
    return " ".join(morse_code)

# 4) Comparing outputs of International Morse Code translator to self-derived Morse code function

if __name__ == '__main__':
    example = "Hello! I'm Alex, and I'm learning data science."
    result_internet = bs4_morse_code(example, 'https://morsedecoder.com/')
    print(result_internet)
    result_self_derived = self_derived_morse(example, morse)
    print(result_self_derived)
    if result_internet == result_self_derived:
        print('You passed!')
    else:
        print('Try again.')