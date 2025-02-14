"""EX02 - This is the one shot wordle assignment."""

__author__ = "730573834"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
prompt_word: str = input("What is your 6-letter guess? ")

guess: int = 0
emoji_boxes: str = ""

while (len(prompt_word) != 6):
    """Check to see if the guess is 6 letters long."""
    prompt_word = input("That was not 6 letters! Try again: ") 

while (guess < len(secret_word)):
    """Looking for matching letters."""
    if (prompt_word[guess] == secret_word[guess]):
        emoji_boxes += GREEN_BOX
    else: 
        var_bool: bool = False
        guess2: int = 0
        while ((var_bool is not True) and (guess2 < len(secret_word))):
            """Looking for letters that occur in both words."""
            if (prompt_word[guess] == secret_word[guess2]):
                var_bool = True
            else:
                guess2 += 1
        if (var_bool is True):
            emoji_boxes += YELLOW_BOX
        else:
            """Looking for no matching letters."""
            emoji_boxes += WHITE_BOX
    guess += 1
print(emoji_boxes)

if (prompt_word == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")


   