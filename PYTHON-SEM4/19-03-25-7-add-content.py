def add_content_and_show_first_three_lines(fpath, extra):
    with open(fpath, 'a') as file:
        file.write(extra)
    with open(fpath, 'r') as file:
        lines = file.readlines()
    print("First 3 lines of the file after adding content:")
    for line in lines[:3]:
        print(line, end='')

fpath = input("Enter the file path: ")
extra = input("Enter extra content to add to the file: ")
add_content_and_show_first_three_lines(fpath, extra)
