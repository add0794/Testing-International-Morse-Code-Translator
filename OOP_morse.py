import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

class MorseCodeTranslator:
    def __init__(self):
        self.morse_alphabet = None
        self.initialize_morse_alphabet()
    
    def initialize_morse_alphabet(self, url='https://morsecodetranslator.com/american-morse-code-translator/'):
        """Initialize the morse code alphabet from web and static data"""
        # Fetch and parse web data
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr')
        characters = soup.find_all('td')
        cols = [ele.text.strip() for ele in characters]
        
        # Create initial DataFrame
        english_letters = [code for code in cols[0::4]]
        morse_code = [code for code in cols[2::4]]
        self.morse_alphabet = pd.DataFrame({
            'English': english_letters,
            'International Morse': morse_code
        })
        
        # Add punctuation marks
        self._add_punctuation_marks()
    
    def _add_punctuation_marks(self):
        """Add punctuation marks to the morse alphabet"""
        punctuation_marks = pd.DataFrame([
            ['.', '.-.-.-'], [',', '--..--'], ['?', '..--..'],
            ['!', '-.-.--'], ['(', '-.--.'], [')', '-.--.-'],
            ['\'', '.----.'], [';', '-.-.-.'], [':', '---.../'],
            ['"', '.-..-.'], ['-', '-....-'], ['/', '-..-.'],
            ['$', '...-..-'], [' ', '/'], ['&', '._...'],    
            ['@', '.__._.'], ['=', '_..._'], ['+', '._._.'],    
            ['_', '..__._']
        ], columns=self.morse_alphabet.columns)
        
        self.morse_alphabet = pd.concat(
            [self.morse_alphabet, punctuation_marks],
            axis=0,
            ignore_index=True
        )
    
    def translate_to_morse(self, text):
        """Translate text to morse code using the stored alphabet"""
        morse_code = []
        
        for char in text:
            row = self.morse_alphabet[
                self.morse_alphabet['English'] == char.upper()
            ]
            if not row.empty:
                morse_code.append(row['International Morse'].values[0])
            else:
                morse_code.append("/")
        
        return " ".join(morse_code)
    
    def verify_with_online_translator(self, text, url='https://morsedecoder.com/'):
        """Verify translation using online translator"""
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            
            word_input = driver.find_element(By.ID, 'input')
            word_input.send_keys(text)
            
            word_output = driver.find_element(By.ID, 'output')
            morse_response = word_output.get_attribute("value")
            
            driver.quit()
            return morse_response
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
    
    def verify_translation(self, text):
        """Compare self-derived translation with online translator"""
        online_result = self.verify_with_online_translator(text)
        self_derived = self.translate_to_morse(text)
        
        if online_result == self_derived:
            return True, "Translation matches online translator"
        return False, "Translation differs from online translator"

def main():
    # Example usage
    translator = MorseCodeTranslator()
    
    example = "Hello! I'm Alex, and I'm learning data science."
    
    # Get translations
    online_result = translator.verify_with_online_translator(example)
    self_derived = translator.translate_to_morse(example)
    
    # Print results
    print("Online translation:", online_result)
    print("Self-derived translation:", self_derived)
    
    # Verify
    is_match, message = translator.verify_translation(example)
    print(f"Verification result: {message}")

if __name__ == '__main__':
    main()