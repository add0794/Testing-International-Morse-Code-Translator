# from bs4 import BeautifulSoup
# import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Applications/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service = s)

driver.get("https://morsedecoder.com/")

content_1 = driver.find_elements_by_class_name("has-text-weight-semibold")
signs = [time.text for time in content_1]
signs.remove('Morse Decoder')
# print(signs)
# print(elements)

content_2 = driver.find_elements_by_css_selector("td")
i = 1
morse = []
while i in range(0, len(content_2)):
    morse.append(content_2[i].text)
    i += 2
# print(morse)

morse_code = {signs[i]:morse[i] for i in range(len(signs))} # Dictionary comprehension
morse_code[" "] = "/"
# print(morse_code)



# = [time.text for time in content]

# print(elements)
# new_elements = [i.split() for i in elements]
# values = dict()
# k = 0
# v = 1
# for i, (k, v) in enumerate(elements):
#     print(i, k, v)
#     k = i + 2
#     v = v + 2
# for i, j in enumerate(new_elements):
#     keys = i + 2
#     value = j + 2
#     values[keys] = value
# signs = dict()
# for i in range(0, len(elements)):
#     elements.split()
#
#     print(element)

#characters > table:nth-child(3) > tbody > tr:nth-child(3) > td:nth-child(2)
# //*[@id="characters"]/table[1]/tbody/tr[3]/td[2]
# <td>....</td>

# response = requests.get(url = "https://morsedecoder.com/")
# url = response.text
# soup = BeautifulSoup(url, "html.parser")

#
# import docx
# # from exceptions import PendingDeprecationWarning
# import os
#
# os.chdir("/Users/adubro4/PycharmProjects/100 Days of Code/Portfolio Project 1 (Day 81)")
# # doc = docx.Document("morse.docx")
# # for i in range(0, len(doc.paragraphs[60].runs)):
# #     print(doc.paragraphs[60].runs[i].text)
#
# def gettext(filename):
#     doc = docx.Document(filename)
#     text = []
#     for paragraph in doc.paragraphs:
#         text.append(paragraph.text)
#     return "\n".join(text)
#
# print(gettext("morse.docx"))
#
# 1.        6     ....
# 2..       7      ...
# 3...       8      ..
# 4....     9       .
# 5.....
# 0        
#
#
#
# morse_code_rules = {
#     'a': '·−',
#     'b': '−···',
#     'c': '−·−·',
#     'd': '−··',
#     'e': '·',
#     'f': '··−·',
#     'g': '−−·',
#     'h': '····',
#     'i': '··',
#     'j': '·−−−',
#     'k': '−·−',
#     'l': '·−··',
#     'm': '−−',
#     'n': '−·',
#     'o': '−−−',
#     'p': '·−−·',
#     'q': '−−·−',
#     'r': '·−·',
#     's': '···',
#     't': '−',
#     'u': '··−',
#     'v': '···−',
#     'w': '·−−',
#     'x': '−··−',
#     'y': '−·−−',
#     'z': '−−··',
#     '0': '−−−−−',
#     '1': '·−−−−',
#     '2': '··−−−',
#     '3': '···−−',
#     '4': '····−',
#     '5': '·····',
#     '6': '−····',
#     '7': '−−···',
#     '8': '−−−··',
#     '9': '−−−−·',
#     ' ': '/'
# }
#
# 1 --       6	. . . .
# 2	. .   	7	  . . .
# 3	. . .   	8	    . .
# 4	. . . . 	9	    .
# 5	. . . . .	0	    
#
# # for paragraph in doc.paragraphs:
# #     text = paragraph.text
# #     new_text = text.split()
# #     print(new_text)
# # print(doc.paragraphs[60].text)
# # paras = doc.paragraphs
# # print(len(paras))
#
# # absFilePath = os.path.abspath(__file__)
# # print(absFilePath)
# # fileDir = os.path.dirname(os.path.abspath(__file__))
# # print(fileDir)
# # parentDir = os.path.dirname(fileDir)
# # print(parentDir)
#
# # os.chdir(os.path.dirname(os.path.abspath(__file__)))
# # print(os.getcwd())
#
# # print(os.getcwd())
# # os.chdir("/Users/adubro4/PycharmProjects/100 Days of Code/Portfolio Project 1 (Day 81)")
# # fileDir = os.path.dirname(os.path.abspath(__file__))
# # os.chdir(fileDir)
# # os.chdir("/Users/adubro4/PycharmProjects/100 Days of Code/Portfolio Project 1 (Day 81)")
# # path = "/Users/adubro4/PycharmProjects/100 Days of Code/Portfolio Project 1 (Day 81)/morse.docx"
# #
# #
# # paras = doc.paragraphs
# # print(len(paras))
# # #
# # # morse = {
# #
# }