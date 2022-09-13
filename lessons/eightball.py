from random import randint

question: str = input("What is your yes/no question?")
response: int = randint(0,2)

if response == 0:
    print("yes, def")
elif response == 1:
    print("ask again later")
elif response == 2:
    print("yes ofc")
else:
    print("my sources say no")
