"""EX02 One-Shot Wordle."""
__author__ = "730335383"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
result: str = ""

count: int = 0
altcount: int = 0

notmatch: bool = True

secret: str = ("python") 

guess = input(f"What is your {len(secret)}-letter guess? ") 

while len(guess) != len(secret): 
    guess = input(f"That was not {len(secret)} letters! Try again: ")


while count < len(guess):

    # reset altcount for new increment 
    altcount = 0
    if guess[count] == secret[count]:
        result = result + green_box
        notmatch = False
    else:
        notmatch = True

    while notmatch:
        if guess[count] == secret[altcount]:
            result = result + yellow_box
            notmatch = False
      
        altcount = altcount + 1

        if altcount == 6:
            break

    if notmatch:
        result = result + white_box
        
    count = count + 1

print(result)

if guess == secret: 
    print("Woo! You got it")
else: 
    print("Not quite. Play again soon! ")  
