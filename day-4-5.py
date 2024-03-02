import random

# define the choices
ROCK = 0
PAPER = 1
SCISSORS = 2

# get user input and convert to corresponding integer
user_input = input("Enter a choice (rock[0], paper[1], scissors[2]): ")
user_action = int(user_input)

# get computer action
computer_action = random.randint(0, 2)

# determine the winner
if user_action == computer_action:
    print("It's a tie!")
elif user_action - computer_action == 1 or (user_action == 0 and computer_action == 2):
    print("You win!")
else:
    print("Computer wins!")

print("Thanks for playing!")