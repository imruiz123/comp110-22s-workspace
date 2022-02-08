"""EX03 Wordle."""
__author__ = "730335383"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8" 


def contains_char(word: str, char: str) -> bool: 
    """So when its true."""
    assert len(char) == 1 
    count = 0
    while count < len(word):
        if word[count] == char: 
            return True 
        count = count + 1 
    return False


def emojified(guess: str, secret: str) -> str:
    """It will print the emjoi."""
    result: str = "" 
    assert len(guess) == len(secret) 
    i = 0
    while i < len(guess):
        if contains_char(secret, guess[i]):
            if secret[i] == guess[i]:
                result = result + green_box
            else:
                result = result + yellow_box
        else:
            result = result + white_box
        i = i + 1
    return result


def input_guess(guess_len: int) -> str:
    """takes input of user"""
    guess: str = input(f"Enter a {guess_len} character word: ")
    i: int = len(guess) 
    while i != guess_len:
        guess = input(f"That wasn't {guess_len} chars! Try again: ")
        i = len(guess)
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    turn: int = 1
    secret: str = "codes"
    while turn <= 6:
        print(f" === Turn {turn}/6 ===")
        guess_temp: str = input_guess(len(secret))
        print(emojified(guess_temp, secret))
        if guess_temp == secret:
            print(f"You won in {turn}/6 turns!")
            break
        elif turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turn = turn + 1