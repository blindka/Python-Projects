# beginner project for self learning - number guessing game
import random #importing random - generating the random number


range = input("Please type number for max of range: ")  
# returns with quotation mark, so we need to convert to number: "25" to 25
if range.isdigit():
    range = int(range)

    if range <= 0:
        print("Please guess number bigger than 0.")
        quit()
else:
    print("Please guess a number.")
    quit()

random = random.randint(0, range) # boundaries of the range (start,end)
guesses = 0

while True:
    guesses += 1
    guess = input("Guess a number:")
    if guess.isdigit():
        guess = int(guess) # remove the quotation mark
    else:
        print("Please type a number.")
        continue

    if guess == random:
        print("You guessed the right number, Well Done!")
        break
    elif guess < random:
        print("Your guess is above the number.")
    else:
        print("Your guess is below the number.")

print("You got it in " ,guesses, " guesses.")