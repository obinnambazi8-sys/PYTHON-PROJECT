word_db= {
    "python" : "It is a high level, interpreted language known for readability",
    "variable" : "A storage location in computer memory, that holds data",
    "Bug" : "An error or fault in a design, development, or operating system",
    "Function" : "A resuable block of organised code, used to perform a single action",
    "object" : "A self contained unit that combines data and behavior",
    "statement" : "A complete set instruction that commands a computer to carry out a specific action.",
    "expression" : "Any combination of variables, operators and function calls that the computer evaluates to produce a single value",
    "value" : "A fi+undamental piece of data that a program can inspect, manipulate or change",
    "data": "An information that a computer processes, manipulate and store to execute instructions.",
    "Algorithm" : "A structured step by step of defined instructions designed to solve a problem or design a specific tasks."
}

def word_lookup():
    word = input("Enter a word to search: ").strip().lower()
    searched = word_db.get(word)
    if searched:
        print(f"{word.capitalize()}: {searched}")
    else:
        print(f"{word}, not found")
# word_lookup()

def add_update_word():
    word= input("Enter a word to search: ").strip().lower()
    defintion = input(f"Enter the definition for '{word}' :").strip()
    if not word or not defintion:
        print("word or defintion cannot be empty")
        return
    word_db[word] = defintion
    print(f"successful '{word}' has been added")
# add_update_word()
# print(word_db)

def all_words():
    if not word_db:
        print("the DB is currently empty")
        return
    print("--- current database content ----") 
    for word,meaning in sorted(word_db.items()):
        print(f"{word.capitalize()}: {meaning}")
    print("--------------")
# all_words()



def main_menu():
    while True:
        print("Welcome to glossary programming dictionary")
        print("1: search for a word")
        print("2: update or add a word")
        print("3: View all words")
        print("4: quit")

        choice = input("Please enter an option[1-4]: ").strip()
        if choice == "1":
            word_lookup()
            break
        elif choice == "2":
            add_update_word()
            break
        elif choice == "3":
            all_words()
            break
        elif choice == "4":
            print("Goodbye, thanks for using our programming dictionary")
            break
        else:
            print("invalid input, pick an option from 1-4")
if __name__ == "__main__":
    main_menu()



