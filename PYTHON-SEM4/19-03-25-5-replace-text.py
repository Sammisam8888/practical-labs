import re

def replace_text_in_file(fpath, old, new):
    with open(fpath, 'r') as file:
        content = file.read()
    updated_content = re.sub(re.escape(old), new, content)
    with open(fpath, 'w') as file:
        file.write(updated_content)

# Assume default file path
fpath = '/home/sammisam8888/Desktop/practical-labs/PYTHON-SEM4/default.txt'
old = input("Enter the text to be replaced: ")
new = input("Enter the new text: ")
replace_text_in_file(fpath, old, new)
