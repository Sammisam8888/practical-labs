import re

def replace_text_in_file(fpath, old, new):
    with open(fpath, 'r') as file:
        content = file.read()
    updated_content = re.sub(re.escape(old), new, content)
    with open(fpath, 'w') as file:
        file.write(updated_content)

def replace_last_name(text, new_last_name):
    updated_text = re.sub(r'\b(\w+)\s(\w+)$', r'\1 ' + new_last_name, text)
    return updated_text

# Assume default file path
fpath = '/home/sammisam8888/Desktop/practical-labs/PYTHON-SEM4/default.txt'
old = input("Enter the text to be replaced: ")
new = input("Enter the new text: ")
replace_text_in_file(fpath, old, new)

text = input("Enter the full name: ")
new_last_name = input("Enter the new last name: ")
print("Updated name:", replace_last_name(text, new_last_name))
