"""EX 01 - Chardle - Input, Variables, and Conditionals."""

__author__ = "730573834"

prompt_word: str = input("Enter a 5-character word: ")
if (len(prompt_word) != 5):
    print("Error: Word must contain 5 characters.")
    exit()
prompt_char: str = input("Enter a single character: ")
if (len(prompt_char) != 1):
    print("Error: Character must be a single letter.")
    exit()

prompt_output: str = "Searching for " + prompt_char + " in " + prompt_word
print(prompt_output)


char_count: int = 0

if (prompt_char == prompt_word[0]):
    print(prompt_char + " found at index 0")
    char_count = char_count + 1
if (prompt_char == prompt_word[1]):
    print(prompt_char + " found at index 1")
    char_count = char_count + 1
if (prompt_char == prompt_word[2]):
    print(prompt_char + " found at index 2")
    char_count = char_count + 1
if (prompt_char == prompt_word[3]):
    print(prompt_char + " found at index 3")
    char_count = char_count + 1
if (prompt_char == prompt_word[4]):
    print(prompt_char + " found at index 4")
    char_count = char_count + 1
if (char_count == 0):
    print("No instances of " + prompt_char + " found in " + prompt_word)
if (char_count == 1):
    print(str(char_count) + " instance of " + prompt_char + " found in " + prompt_word)
if (char_count > 1):
    print(str(char_count) + " instances of " + prompt_char + " found in " + prompt_word)