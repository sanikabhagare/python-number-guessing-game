import random

# The system picks a random number betn 1 to 100

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100. Can you guess it?")

# This loop will run forever until the player guesses correctly
while True:
    # Ask the user for their guess
    guess = int(input("Enter your guess: "))
    
    # Check if the guess is correct, too high, or too low
    if guess == secret_number:
        print(" Congratulations! You guessed the right number!")
        break  # This stops the loop and ends the game
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
