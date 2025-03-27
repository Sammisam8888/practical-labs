"""
Q1 - wap to create a banki class whihc contains account no and balance. use abstraction method to update balance after deposit and withdraw. if less balance is present then show insufficient balance error
Q2 - write 3 sentences from user input in a text file

Q3 -Write a program using file handling to check if a file exists or not. If it exists, delete it and create another file with the same name (using "x" mode).

Q4 -Write a program that uses a regular expression to validate an email address.conditions (starting - no capital letter, atleast 1 or 2 number and letter, atleast 8 letter before special character)

Q5 - Write a program to replace the last name of a person using a regular expression.

Q6 - Write a program to demonstrate how to read data from a text file and overwrite it.

Q7 -Write a program to demonstrate how to add data to a text file and display the first 3 lines of the updated file.
"""

import re

a = "Winter is coming."

b = re.search("^Winter.*.$", a)
if b:
    print("String Matched")
else:
    print("No")

b = re.findall("i", a)
print(b)

c = re.search("\s", a)
print("Blank space at ", c.start())

d = re.split("\s", a)
print(d)

e = re.sub("Winter", "Dragon", a)
print(e)

e1 = re.sub("\s", "Targerian", a, 2)
print(e1)