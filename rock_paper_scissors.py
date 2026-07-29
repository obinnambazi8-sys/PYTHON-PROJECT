import random
Rock = 0
Paper = 1
scissors = 2
choices = ["Rock","Paper","Scissors"]

user_decisions=int(input("What do you choose? type 0 for Rock, 1 for paper or 2 for Scissors.: "))
computer_choice= random.randint(0,2)
print(f"You chose:{choices[user_decisions]}")
print(f"computer chose: {choices[computer_choice]}")

if user_decisions == computer_choice:
    print("It's a draw!")

elif user_decisions == 0 and computer_choice == 2:
    print(f"computer chose: scissors, you win!")
elif user_decisions ==1 and computer_choice ==0:
    print(f"computer chose: rock, you win!")
elif user_decisions ==2 and computer_choice == 1:
    print(f"computer chose: paper, you win!")
else:
    print("the end")



