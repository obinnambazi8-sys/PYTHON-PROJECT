import random
choice = ["rock","paper","scissors"]
players_score = 0
computer_score = 0

print("Welcome to rock paper scissors game.")
print("rock wins against scissors, scissors wins against paper and paper wins against rock ")

while True:
    players_choice = input("What do you choose? Rock, paper or scissors or 'quit' to end the game: ")
    if players_choice.lower() == 'quit':
        break
    if players_choice not in choice:
        print("invalid choice, please try again")
        continue
    computer_choice = random.choice(choice)
    print(f"you chose: {players_choice}")
    print(f"computer chose: {computer_choice}")

    if players_choice == computer_choice:
        print("Its a draw")
    if players_choice == 'rock' and computer_choice == 'scissors' or players_choice =='paper' and computer_choice == 'rock' or players_choice == 'scissors' and computer_choice == 'paper':
        print("you are a winner")
    else:
        computer_score += 1