# beginner project for self learning - quiz game

playing = input("Do you want to play a game? ")

if playing.lower() != "yes": #lower - convert the text to lower text, example: YES -> yes etc.
    print("You choose not to play, type 'yes' in order to play.")
    quit()

print("Okay! Let's play.")
score = 0

answer = input("What hours there is in a day? ")
if answer == "24":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! \nThe correct answer is: 24")

answer = input("How many days are there in december? ")
if answer == "31":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! \nThe correct answer is: 31")

answer = input("What many months are there in a year? ")
if answer == "12":
    print("Correct Answer!")
    score += 1
else:
    print("Wrong Answer! \nThe correct answer is: 12")

print("You answered " +str(score)+ " questions correctly!")
print("You answered " +str((score/3) * 100)+ "% of the questions correctly!")
