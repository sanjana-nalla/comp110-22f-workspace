"""EX03 - Structured Wordle Assignment."""

__author__ = "730573834"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(given_str: str, search_char: str) -> bool:
    assert len(search_char) == 1
    """This function iterates through the string, given_str, as it checks to see if each letter of string is equal to the comparison character, search_char. """
    while (given_str > ""):
        if (given_str[0] == search_char):
            return True
        else:
            given_str = given_str[1:]
    return False


def emojified (prompt_word: str, secret_word: str) -> str:
    assert len(prompt_word) == len(secret_word)
    
    guess: int = 0
    emoji_boxes: str = ""

    while (guess < len(secret_word)):
        if (prompt_word[guess] == secret_word[guess]):
            emoji_boxes += GREEN_BOX
        elif (contains_char(secret_word, prompt_word[guess]) is True):
            emoji_boxes += YELLOW_BOX
        else:
            emoji_boxes += WHITE_BOX
        guess += 1

    return emoji_boxes

def input_guess (word_num_letter: int) -> str:
    prompt_word = input(f"Enter a {word_num_letter} character word: ")
    while (len(prompt_word) != word_num_letter):
        prompt_word = input(f"That wasn't {word_num_letter} chars! Try again: ")
    return prompt_word

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    correct: bool = False
    
    while ((turns <= 6) and (correct is False)):
        print(f"=== Turn {turns}/6 ===")
        guessed: str = input_guess(len(secret_word))
        print(emojified(guessed, secret_word))

        if (guessed == secret_word):
            correct = True
            print(f"You won in {turns}/6 turns!")
            quit()
        turns += 1

        if (turns > 6):
            print("X/6 - Sorry, try again tomorrow!")
            quit()
