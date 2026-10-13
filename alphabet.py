word = input("Enter a character or word: ")
if word.isalpha():
    print("Alphabet")
elif word.isdigit():
    print("Number")
elif not word.isalnum() and not word.isspace():
    print("Special character")
else:
    print("Mixed input or whitespace")