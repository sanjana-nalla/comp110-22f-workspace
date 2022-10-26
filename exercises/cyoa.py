"""This is my exercise EX06 - Create Your Own Adventure!"""

__author__ = "730573834"


points: int = 0
player: str = ""
book_emoji: str = "\U0001F4DA"


def main() -> None:
    """This function is the main function which determines the order of the following functions run in and global variables are declared in this function."""
    global points
    global player
    global book_emoji

    greet()
    three_directions()
    main_questions()
    results()
    game_loop()


def greet() -> None:
    """This function introduces the game to the player and takes in user input to get the user name to use throughout the game."""
    global player 

    print("Hello! Let's find out what field you should study!")
    player = input("What is your name? ")
    print(f"Nice to play with you, {player}")


def three_directions() -> None:
    """This function provides the user three options to choose from using user input and using the if-else tree, the user is lead in different directions."""
    direction: str = input("Do you want to read the instructions and then take the quiz, go straight to the quiz, or get your results? \nPlease respond with 'instructions', 'quiz', or 'results'. Your Answer: ")
    if (direction == "instructions" or direction == "Instructions"):
        start_game()
    elif (direction == "quiz" or direction == "Quiz"):
        main_questions()
        results()
        game_loop()
        exit()
    elif (direction == "results" or direction == "Results"):
        results()
        exit()
    else:
        print("Invalid Response. Try again.")
        three_directions()


def instruct_plus_response() -> bool:
    """This function takes in user input and returns a boolean variable through a if-else tree and is called in start_game."""
    print("Here are the instructions for the game.")
    print("1) Be truthful in your responses in order to get a accurate response.")
    print("2) Answer each question in the quiz with the letter of the answer choice without the parantheses after this. Example: answer with 'a' or 'A'.")
    
    understood: str = input("Did you understand the instructions? ")
    if (understood == "Yes" or understood == "yes"):
        return True
    elif (understood == "No" or understood == "no"):
        return False
    else:
        print("Invalid Response.")
        return False

    
def start_game() -> None:
    """This function takes the boolean return variable from instruct_plus_response() function to determine whether the user wants to play the game using a if-else tree."""
    if (instruct_plus_response() is True):
        print("\nGreat! Let's start the game.\n")
    else:
        print("\nRe-read the instructions.")
        instruct_plus_response()
        print("\nYou have read the instructions twice, let's start the game and learn as we go!\n")


def first_q_and_a() -> None:
    """This question takes in user input and adds points to the global variable points."""
    question_one: str = input(f"{player}, what do you like more? \na) STEM \nb) Humanities \nYour Answer: ")
    global points

    if (question_one == "a" or question_one == "A"):
        points += 100
        print(f"\nTotal points: {points}")
    elif (question_one == "b" or question_one == "B"):
        points += 10
        print(f"\nTotal points: {points}")
    else:
        print("Invalid Response. Try again.")
        first_q_and_a()


def second_q_and_a() -> None:
    """This question takes in user input and adds points to the global variable points."""
    global points

    if (points == 100):
        question_second_a: str = input(f"\n{player}, what do you like better? \na) science  \nb) technology \nc) engineering \nd) mathematics \nYour Answer: ")
        if (question_second_a == "a" or question_second_a == "A"):
            points += 5
            print(f"\nTotal points: {points}")
        elif (question_second_a == "b" or question_second_a == "B"):
            points += 10
            print(f"\nTotal points: {points}")
        elif (question_second_a == "c" or question_second_a == "C"):
            points += 15
            print(f"\nTotal points: {points}")
        elif (question_second_a == "d" or question_second_a == "D"):
            points += 20
            print(f"\nTotal points: {points}")
        else:
            print("Invalid Response. Try again.")
            second_q_and_a()
    else: 
        question_second_b: str = input(f"\n{player}, what do you like better? \na) Literature or Languages \nb) Social Sciences \nc) History \nd) Arts \nYour Answer: ")
        if (question_second_b == "a" or question_second_b == "A"):
            points += 5
            print(f"\nTotal points: {points}")
        elif (question_second_b == "b" or question_second_b == "B"):
            points += 10
            print(f"\nTotal points: {points}")
        elif (question_second_b == "c" or question_second_b == "C"):
            points += 15
            print(f"\notal points: {points}")
        elif (question_second_b == "d" or question_second_b == "D"):
            points += 20
            print(f"\nTotal points: {points}")
        else:
            print("Invalid Response. Try again.")
            second_q_and_a()


def third_q_and_a() -> None:
    """This question takes in user input and adds points to the global variable points."""
    global points

    question_three: str = input(f"\n{player}, what skills are you proficient at? \na) Critical Thinking and/or Analysis \nb) Problem-Solving \nc) Communication \nd) Creativity \nYour Answer: ")
    
    if (question_three == "a" or question_three == "A"):
        points += 5
        print(f"\nTotal points: {points}")
    elif (question_three == "b" or question_three == "B"):
        points += 10
        print(f"\nTotal points: {points}")
    elif (question_three == "c" or question_three == "C"):
        points += 15
        print(f"\nTotal points: {points}")
    elif (question_three == "d" or question_three == "D"):
        points += 20
        print(f"\nTotal points: {points}")
    else:
        print("Invalid Response. Try again.")
        third_q_and_a()


def fourth_q_and_a() -> None:
    """This question takes in user input and adds points to the global variable points."""
    global points

    import random 
    question_four: str = input(f"\n{player}, what number do you like best? \na) {random.randint(1, 50)} \nb) {random.randint(100, 200)} \nc) {random.randint(500, 1000)} \nd) {random.randint(1000,2000)} \nYour Answer: ")

    if (question_four == "a" or question_four == "A"):
        points += 5
        print(f"\nTotal points: {points}")
    elif (question_four == "b" or question_four == "B"):
        points += 10
        print(f"\nTotal points: {points}")
    elif (question_four == "c" or question_four == "C"):
        points += 15
        print(f"\nTotal points: {points}")
    elif (question_four == "d" or question_four == "D"):
        points += 20
        print(f"\nTotal points: {points}")
    else:
        print("Invalid Response. Try again.")
        fourth_q_and_a()


def fifth_q_and_a(points: int) -> int:
    """This question takes in user input and adds points to the global variable points."""
    question_five: str = input(f"\n{player}, how would people describe you? \na) Hardworking \nB) Outgoing/Energetic \nc) Inquistive \nd) Empathetic \nYour Answer: ")

    if (question_five == "a" or question_five == "A"):
        points += 5
        print(f"\nTotal points: {points}")
    elif (question_five == "b" or question_five == "B"):
        points += 10
        print(f"\nTotal points: {points}")
    elif (question_five == "c" or question_five == "C"):
        points += 15
        print(f"\nTotal points: {points}")
    elif (question_five == "d" or question_five == "D"):
        points += 20
        print(f"\nTotal points: {points}")
    else:
        print("Invalid Response. Try again.")
        fifth_q_and_a(points)
    return points


def main_questions() -> None:
    """This function consolidates all the question functions into one main function which is also called in the main() function."""
    global points 

    first_q_and_a()
    second_q_and_a()
    third_q_and_a()
    fourth_q_and_a()
    points = fifth_q_and_a(points)


def results() -> None:
    """This function outputs the results, the potential majors, for the user based on the number of total points using a very extensive if-else tree."""
    global points 
    global player
    print(f"\n{player}, you have {points} points!")

    if (points == 0):
        print("Try being undecided! :))")
    elif (points < 30):
        print(f"You should be a {book_emoji}English{book_emoji} major, {book_emoji}Language{book_emoji} major, or {book_emoji}Linguistics{book_emoji} major!")
    elif (30 <= points < 45):
        print(f"You should be a {book_emoji}Sociology{book_emoji} major, {book_emoji}Anthropology{book_emoji} major, or {book_emoji}Cultural Studies{book_emoji} major!")
    elif (45 <= points < 60):
        print(f"You should be a {book_emoji}Psychology{book_emoji} major, {book_emoji}Cognitive Science{book_emoji} major, or {book_emoji}Behavioral Science{book_emoji} major!")
    elif (60 <= points < 75):
        print(f"You should be a {book_emoji}History{book_emoji} major, {book_emoji}Communication Studies{book_emoji} major, or {book_emoji}Education{book_emoji} major!")
    elif (75 <= points < 90):
        print(f"You should be a {book_emoji}Fine Arts{book_emoji} major, {book_emoji}Studio Arts{book_emoji} major, or {book_emoji}Dramatic Arts{book_emoji} major!")
    elif (90 <= points < 120):
        print(f"You should be a {book_emoji}Business{book_emoji} major, {book_emoji}Economics{book_emoji} major, or {book_emoji}Statistics{book_emoji} major!")
    elif (120 <= points < 135):
        print(f"You should be a {book_emoji}Biology{book_emoji} major, {book_emoji}Chemistry{book_emoji} major, or {book_emoji}Physics{book_emoji} major!")
    elif (135 <= points < 150):
        print(f"You should be a {book_emoji}Math{book_emoji} major, {book_emoji}Environmental Science{book_emoji} major, or {book_emoji}Engineering{book_emoji} major!")
    elif (150 <= points < 165):
        print(f"You should be a {book_emoji}Architecture{book_emoji} major, {book_emoji}Health Policy and Management{book_emoji} major, or {book_emoji}Biostatistics{book_emoji} major!")
    elif (165 <= points < 180):
        print(f"You should be a {book_emoji}Computer Science{book_emoji} major, {book_emoji}Neuroscience{book_emoji} major, or {book_emoji}Astrophysics{book_emoji} major!")
    else:
        print("Try consolidating your interests more!")


def game_loop() -> None:
    """This function takes user input to see if the user would like to play again using a if else tree."""
    global player
    global points 
    points = 0
    play_again: str = input(f"{player}, would you like to play again? \n")

    if (play_again == "yes" or play_again == "Yes"):
        print("Yay! Let's play again.")
        main()
    elif (play_again == "maybe" or play_again == "Maybe"):
        import random
        random_number: int = random.randint(0, 200)
        if (random_number < 100):
            print(f"Choosing maybe results in the use of a random number generator which chooses whether you play again or not.\nA number under 100 allows you to play again while any other number ends the game/quiz.\nYour number was {random_number}.")
            print(f"Let's do the questions again, {player}!")
            main_questions()
            results()
        else:
            print(f"Choosing maybe results in the use of a random number generator which chooses whether you play again or not.\nA number under 100 allows you to play again while any other number ends the game/quiz.\nYour number was {random_number}.")
            print(f"Maybe, next time. Goodbye, {player}!") 
    elif (play_again == "no" or play_again == "No"):
        print(f"Maybe, next time. Goodbye, {player}!")
    else:
        print("Invalid Response. Try again.")
        game_loop()


if __name__ == "__main__":
    main()