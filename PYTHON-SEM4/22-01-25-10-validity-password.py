password=input("Enter your password: ")
pwd=input("Re-enter your password: ")
if pwd!=password:
    print("Passwords do not match!")
else :
    print("Passwords match!")
    characters=0
    numbers=0
    upper=0
    lower=0

    for i in pwd:
        if i.isdigit():
            numbers+=1
        elif not(i.isalpha()):
            characters+=1
        elif i.isupper():
            upper+=1
        elif i.islower():
            lower+=1

    if characters==0 or numbers==0 or lower==0 or upper==0 or len(pwd)<8:
        print("Password not valid. it contain at least one character, one number, one capital and one small number.Password should be at least 8 characters long.")
    else:
        print("Password is strong.")

    