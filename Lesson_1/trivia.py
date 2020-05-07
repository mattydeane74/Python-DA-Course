# This program is a Trivia game
import time

print()
time.sleep(2)
print("Hello and Welcome to a great game of Trivia.")
time.sleep(2)

print("Let's introduce each other first. My name is Ms. Robot!")
time.sleep(2)

print("What is your name?")
time.sleep(1)

name = input("Please type your name here: ")
for i in range(2):
    print("Processing...")
    time.sleep(1)

print(f"Welcome, {name}. It is a pleasure to meet you!")
time.sleep(3)
         
print(f"Are you ready to play some trivia today, {name}.")
time.sleep(1)
print("We are going to have 5 questions.")
time.sleep(1)
print("Good luck! I hope you are ready!")

wins = 0

loss = 0

time.sleep(2)
print("-" * 70)
print("-" * 30 + " Question 1! " + "-" * 30)
print("-" * 70)

#### Let's get started with some Trivia

time.sleep(1)
print("What is a baby kangaroo called?")
answer1 = input("Please type your answer here: ")

if answer1.lower() == 'joey':
    print("That's correct. Great work!")
else:
    print("Sorry Dude")
    print("The answer is Joey :)")


if answer1.lower() == 'joey':
    wins += 1
else:
    loss += 1

print("Cool, let's keep going!")

time.sleep(2)
print("-" * 70)
print("-" * 30 + " Question 2! " + "-" * 30)
print("-" * 70)


time.sleep(1)
print("What term is used to describe food that has been prepared according to Jewish dietary laws?")
answer2 = input("Please type your answer here: ")

if answer2.lower() == 'kosher':
    print("That's correct. Great work!")
else:
    print("Sorry Dude")
    print("The answer is Kosher :)")


if answer2.lower() == 'kosher':
    wins += 1
else:
    loss += 1

print("Cool, let's keep going!")

time.sleep(2)
print("-" * 70)
print("-" * 30 + " Question 3! " + "-" * 30)
print("-" * 70)




time.sleep(1)
print("Prior to the introduction of the Euro, the Lira was the currency of which European country?")
answer3 = input("Please type your answer here: ")

if answer3.lower() == 'italy':
    print("That's correct. Great work!")
else:
    print("Sorry Dude")
    print("The answer is Italy :)")


if answer3.lower() == 'italy':
    wins += 1
else:
    loss += 1

print("Cool, let's keep going!")


time.sleep(2)
print("-" * 70)
print("-" * 30 + " Question 4! " + "-" * 30)
print("-" * 70)


time.sleep(1)
print("Tennis star Serena Williams won which major tournament while pregnant with her first child?")
answer4 = input("Please type your answer here: ")

substring = 'australia'
fullstring = answer4.lower()

if substring in fullstring:
    print("That's correct. Great work!")
else:
    print("Sorry Dude")
    print("The answer is Australian Open :)")


if substring in fullstring:
    wins += 1
else:
    loss += 1

print("Cool, let's keep going!")

time.sleep(2)
print("-" * 70)
print("-" * 30 + " Question 5! " + "-" * 30)
print("-" * 70)



time.sleep(1)
print("Over half of South America’s western coast is occupied by which country?")
answer5 = input("Please type your answer here: ")

if answer5.lower() == 'chile':
    print("That's correct. Great work!")
else:
    print("Sorry Dude")
    print("The answer is Chile :)")


if answer5.lower() == 'chile':
    wins += 1
else:
    loss += 1

print("Great work, time to tally the results!")

print(f"you got {wins} from 5!")


if wins > loss:
    
    print("Congrats, you got more correct than you got wrong, you are Trivia gun!!! ;)")
    time.sleep(3)
    print("This was a lot of fun, I hope you come visit me again soon. Take care!")
else:
    print("back luck, good luck next time.")
    time.sleep(3)
    print(f"This was a lot of fun {name}, I hope you come visit me again soon. Take care!")