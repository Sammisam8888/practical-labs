with open("user_sentences.txt", "w+") as file:
    for i in range(3):
        sent = input(f"Enter sentence {i+1}: ")
        file.write(sent + "\n")
    print("File writing complete, The contents of the file are : ")
    file.seek(0)  # Move the cursor to the beginning of the file before reading
    print(file.read())