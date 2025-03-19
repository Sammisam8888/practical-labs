with open("user_sentences.txt", "w") as file:
    for i in range(3):
        sent = input(f"Enter sentence {i+1}: ")
        file.write(sent + "\n")
