# Testing International Morse Code Translator

There are two ways to test if two *International* Morse code messages match.

<!-- The first is developed by using Selenium to get its alphabet entirely by scraping from this website: https://morsedecoder.com/. Using an input message as its output, the Morse code is created using the nested list from the Selenium-derived alphabet. The second is developed by sending that message to the Text input field from the aforementioned website and returning the output Morse code. -->

The first is redundant and unnecessarily confusing, so I have not developed such a program. In this type of program, the input text from the [website](https://morsedecoder.com/) is translated, and the output text is stored as a variable. That same input text is scraped using Selenium, then a Morse alphabet, whether scraped or downloaded, is used to turn the text to Morse sode by software program. The two results are compared against each other to see if they're the same.

The [second](https://github.com/add0794/Testing-International-Morse-Code-Translator/blob/main/procedural_morse.py) is more efficient by creating a Morse alphabet using Beautiful Soup, a version of which can be found [here](https://www.hobby-hour.com/electronics/morse_code.php). The (English) input text will result in its own Morse translation, using the website described above. The input text is additionally used to translate into Morse with the Python-derived Morse alphabet. The results of the translator and the Python software program are compared against each other to see if they're the same.

An object-oriented version is available from the second version, though given the straightforward nature of this assignment, a procedural approach does the job just fine, if not better.

Learn more about Morse code [here](https://www.babbel.com/en/magazine/how-does-morse-code-work), as well as how it's applied in other languages. A detailed description can be found [here](https://github.com/add0794/Testing-International-Morse-Code-Translator/blob/main/International%20Morse%20Code.docx), too.
