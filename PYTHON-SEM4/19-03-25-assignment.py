"""
Q1 - wap to create a banki class whihc contains account no and balance. use abstraction method to update balance after deposit and withdraw. if less balance is present then show insufficient balance error
Q2 - write 3 sentences from user input in a text file
Q3 - wap to check using file handling if a file exist or not. if the file is existing,remove that file and create the same deleted file name using file handling method (x mode)
Q4 - wap using regex to validate an emai; address. conditions (starting - no capital letter, atleast 1 or 2 number and letter, atleast 8 letter before special character)
Q5 - wap to replace text file using regex Rahul Sharma -> Rohit Sharma
Q6 - wap to demonstrate how to read data from a text file and after reading text file overwrite it 
Q7 - wap to demonstrate how to add some extra content to existing file and show the first 3 line of your operated file

"""

#regular expression
import re

#^ - indicates starting, $- indicates ending
s="Winter is coming"
b=re.search("Winter",s)
print(b)
print(type(b))

e=re.sub("Winter","Dragon",s)
print(s) #no replacement in original string
print(e) #new updated string .