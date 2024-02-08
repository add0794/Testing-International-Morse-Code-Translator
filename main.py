"""
You will use what you've learnt to create a text-based (command line) program that takes any String input and
converts it into Morse Code.

You've created plenty of text-based programs in Days 1 -10, so look back at some of those projects if you
don't remember what a text-base program looks like.

https://en.wikipedia.org/wiki/Morse_code

The design, functionality, code style is all up to you. You're wearing the big-girl/big-boy pants now. So you
get to decide.
"""

# Source: https://morsedecoder.com/

from morse import morse_code

# with open("morse.doc", "rb") as file:
#     data = file.read()
#     print(data)
#     file.close()

script = input("What would you like to tell me? ")
script_upper = script.upper()
print(script_upper)
letters = list(script_upper)
print(letters)
i = 0
sent = []
while i < len(letters):
    sent.append(morse_code[letters[i]])
    i += 1
print(sent)

morse = " ".join(str(x) for x in sent)
print(morse)
# for _ in sent:
#     new_string = _.replace("/", " ")
# print(sent)
#
# print(morse)
# sent = [morse_code[letter] for letter in morse_code.keys() if letter in letters]
# for _ in morse_code.keys():
#     if _ in letters:
#         sent.append(morse_code[_])
# [morse_code[letter] for letter in letters if letter in morse_code.keys()]
# print(sent)


# 1) letter repeats itself 2) make letter capitalized
# space after each letter; / after each word