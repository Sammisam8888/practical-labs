def read_and_overwrite_file(fpath):
    with open(fpath, 'r') as f:
        content = f.read()
    print("Original Content:\n", content)
    new_content = input("Enter new content to overwrite the file: ")
    with open(fpath, 'w') as f:
        f.write(new_content)

fpath = input("Enter the file path: ")
read_and_overwrite_file(fpath)
