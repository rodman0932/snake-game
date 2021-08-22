print("Welcome to my snake question quiz!")

playing = input("do you wnat to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play:)")
score = 0

answer = input("How many grams does a female have to be in order to breed? ")
if answer.lower() == "1500":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many grams does a male have to be in order to breed? ")
if answer.lower() == "600":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("On average how long do the eggs have to incubate? ")
if answer.lower() == "54":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("What is the average temperature in the enclosure? ")
if answer.lower() == "90":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4) * 100) + " %")


