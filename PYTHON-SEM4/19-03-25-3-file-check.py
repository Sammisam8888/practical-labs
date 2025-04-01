import os

def replace(fname):
    if os.path.exists(fname):
        os.remove(fname)
        print(f"{fname} removed.")
    else:
        print(f"{fname} does not exist.")
    with open(fname, "x") as file:
        file.write("This is a new file created after deletion.")
        print(f"{fname} created.")

fname = input("Enter the file name: ")
replace(fname)
