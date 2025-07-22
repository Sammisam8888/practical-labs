x = input("Enter a sentence: ")
words = x.split()
reversed = words[::-1]
result = " ".join(reversed)
print("Reversed sentence:", result)