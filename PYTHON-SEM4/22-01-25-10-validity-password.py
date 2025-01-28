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
        print("Password is not valid. it must contain at least one special character, one number, one capital and one small letter.Password should be at least 8 characters long.")
    else:
        print("Password is strong and valid.")

    