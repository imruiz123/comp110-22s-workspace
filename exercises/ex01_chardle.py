"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730335383"

word: str = input("Enter a 5-character word: ")
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if (len(letter) != 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + word) 

increment_count = 0
if (word[0] == letter):
    print(letter + " found at index 0")
    increment_count = increment_count + 1
if (word[1] == letter): 
    print(letter + " found at index 1")
    increment_count = increment_count + 1
if (word[2] == letter): 
    print(letter + " found at index 2")
    increment_count = increment_count + 1
if (word[3] == letter): 
    print(letter + " found at index 3")
    increment_count = increment_count + 1
if (word[4] == letter): 
    print(letter + " found at index 4")
    increment_count = increment_count + 1
if increment_count == 0:
    print("No instances of " + letter + " found in " + word)
else:
    if increment_count > 1:
        print(increment_count, "instances of " + letter + " found in " + word)
    else:
        print(increment_count, "instance of " + letter + " found in " + word)
