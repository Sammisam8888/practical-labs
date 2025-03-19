import re

def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        content = file.read()
    updated_content = re.sub(re.escape(old_text), new_text, content)
    with open(file_path, 'w') as file:
        file.write(updated_content)

# Assume default file path
file_path = '/home/sammisam8888/Desktop/practical-labs/PYTHON-SEM4/default.txt'
old_text = input("Enter the text to be replaced: ")
new_text = input("Enter the new text: ")
replace_text_in_file(file_path, old_text, new_text)
