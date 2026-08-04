import random

name=input("Please your name: ").title()
print(f"Hello, {name} goodluck")

words= ["school", "ferrari","banana","porsche","Barcelona"]
word = random.choice(words)
print(word)
print("\nGuess the characters")

guesses = ""
attempts = 70
while attempts > 0:
    failed = 0
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
        else:
            print("_", end=" ")
            failed +=1
    print()
    if failed == 0:
        print(f"Congratulations you win!, The word is {word} break")
    guess =input("Guess a character: ").lower()
    if len(guess) !=1:
        continue
    if guess in guesses:
        print("You already guessed that character. ")
        continue
    guesses += guess
    if guesses not in word:
        attempts -= 1
        print(f"Wrong,you have {attempts} more to guess")
        if attempts == 0:
            print(f"You lost the word is: {word}")
        



