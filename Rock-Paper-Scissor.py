import random

print("Let's play! Write either rock, paper, or scissors!")
print("Rock..Paper..Scissors..Shoot!")
play = ["rock", "paper", "scissors"]
op = input()
 
if op == "rock":
    print("I play " + play[1])
elif op == "paper":
    print("I play " + play[2])
elif op == "scissors":
    print("I play " + play[0])
else:
    print("Try again, I think you have a typo in your answer choice!")
    int = 0
if(int != 0):
    result = ["Sorry, you lose!", "Better luck next time!", "You thought lol", "It's ok, I'm built different"]
    print(random.choice(result))