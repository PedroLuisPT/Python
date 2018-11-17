import random
number = random.randint(0,1000)
guess = -1
print("Guess the number!")
while guess != number:
    guess = int(input("Will it be..."))
    if guess == number:
        print("Urray! You Guessed it!")
    elif guess < number:
        print("It's bigger...")
    elif guess > number:
        print("Not that big.")
