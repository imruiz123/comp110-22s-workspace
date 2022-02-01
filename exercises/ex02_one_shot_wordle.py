"""EX02 One-Shot Wordle."""


_author_ = "730335383"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
RESULT: str = ""

COUNT: int = 0
ALTCOUNT: int = 0

NOTMATCH: bool = True

SECRET: str = ("python") 

guess = input(f"What is your {len(SECRET)}-letter guess? ") 

while len(guess) != len(SECRET): 
    guess = input(f"That was not {len(SECRET)} letters! Try again: ")


while COUNT < len(guess):

    # reset altcount for new increment 
    ALTCOUNT = 0
    if guess[COUNT] == SECRET[COUNT]:
        RESULT = RESULT + GREEN_BOX
        NOTMATCH = False
    else:
        NOTMATCH = True

    while NOTMATCH:
        if guess[COUNT] == SECRET[ALTCOUNT]:
            RESULT = RESULT + YELLOW_BOX
            NOTMATCH = False
      
        ALTCOUNT = ALTCOUNT + 1

        if ALTCOUNT == 6:
            break

    if NOTMATCH:
        RESULT = RESULT + WHITE_BOX
        
    COUNT = COUNT + 1

print(RESULT)

if guess == SECRET: 
    print("Woo! You got it")
else: 
    print("Not quite. Play again soon! ")  
