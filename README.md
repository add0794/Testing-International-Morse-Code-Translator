# Testing International Morse Code Translator

There are two ways to test if two *International* Morse code messages match.

<!-- The first is developed by using Selenium to get its alphabet entirely by scraping from this website: https://morsedecoder.com/. Using an input message as its output, the Morse code is created using the nested list from the Selenium-derived alphabet. The second is developed by sending that message to the Text input field from the aforementioned website and returning the output Morse code. -->

The first is redundant and unnecessarily confusing, so I won't go ahead with that program. In this one, the input text from [website](https://morsedecoder.com/) is translated, and the output text is stored as a variable. That same (English) input text is scraped using Selenium, then a Morse alphabet, whether scraped or downloaded, is used to turn that text to Morse sode. The translor's results are compared against the Python code's output, and the translator's output should be the same.

The second is more efficient by first creating a Morse alphabet using Beautiful Soup, a version of which can be found [here](https://www.hobby-hour.com/electronics/morse_code.php). The (English) input text, scraped from Selenium, will result in its own Morse translation, and then it's used to translate into Morse with its own separate Python function. Again, the translator's results are compared against the Python code's output, and the translator's output should be the same.

An object-oriented version is available from the second version, though given the straightforward nature of this assignment, a procedural approach does the job just fine, if not better.

Learn more about Morse code [here](https://www.babbel.com/en/magazine/how-does-morse-code-work), as well as how it's applied in other languages.
