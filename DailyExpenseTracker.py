items_price ={
    "shoes" : 5.00,
    "food" : 100.00,
    "keys" : 40.00,
    "games" : 20.00
}

def add_expense():
    item= input("Enter an item: ").strip().lower()
    price= float(input("Enter a price: "))
    if not item or not price:
        print("Unsuccessful entry, try again")
        return
    items_price[item] = price
    print(f"{item} and {price} has been added.")
# add_expense()


def total_expense():
    total = sum(items_price.values())
    print(total)
# total_expense()

def view_expenses():
    if not items_price:
        print("Error chose the correct item")
        return
    for items, prices in sorted(items_price.items()):
        print(f"{items.capitalize()} : {prices}")
# view_expenses()

def main_menu():
    while True:
        print("Welcome to your Daily expense Tracker")
        print("1: Enter an item and price")
        print("2: See the total of your expenses")
        print("3: View your expenses")

        option= input("Enter an option: Select from 1 - 3: ")
        if option == "1":
            add_expense()
        elif option == "2":
            total_expense()
        elif option == "3":
            view_expenses()
        else:
            print("Thank you for using our daily expense app")
            break
main_menu()
        