# def to_do_list():
#     choice = input("Type 'yes' to make a list or 'no' to quit: ") 
#     lists = []
#     while choice!='no':
#         # choice = input("Type 'yes' to make a list or 'no' to quit: ") 
#         questions=input("What is your to do lists? \n")
#         lists.append(questions)
#         choice = input("Do you want to add another item?: ") 

#     print(lists)
# to_do_list()
#----------------------------------------------------------------------------------------------------------------------------
# def my_to_do_list():
#     items = []
#     while True:
#         print("1:  Add Item")
#         print("2: Remove Item")
#         print("3: Show Items")
#         print("4: Edit")
#         print("5: Quit")
#         decision = input("Enter your choice: ")
#         if decision == "1":
#             item = input("Enter item: ")
#             items.append(item)
#         elif decision == "2":
#             item = input("Enter an item to be removed: ")
#             if item in items:
#                 items.remove(item)
#                 print(f"{item} deleted successfully") 
#             else:
#                 print(f"{item} not found")
#         elif decision == "3":
#             print("available items: ")
#             for item in items:
#                 print(f"_ {item}")
#         elif decision == "4":
#             edit = input("Enter what you want to replace: ")

#             for item in items:
#                 if edit in items:
#                     edited_item = input("Enter the correct item: ")
#                     index = items.index(edit)
#                     items[index] = edited_item
#                     # items.insert(1,edit)
#                     # items[item] = edit
#                     # break
#                 else:
#                     print("Item not found")
                
#         elif decision == "5":
#             break
#         else:
#             print("Invalid choice")
# my_to_do_list()

# #---------------------------------------------------------------------------------------------------------------------
def my_to_do_list():
    items = []
    while True:
        print("1:  Add Item")
        print("2: Remove Item")
        print("3: Show Items")
        print("4: Edit")
        print("5: Mark item as Completed")
        print("6: Quit")
        decision = input("Enter your choice: ")
        if decision == "1":
            item = input("Enter item: ")
            items.append({
                "task": item,
                "completed" : False,
            })
            print("item added successfully")
        elif decision == "2":
            info = input("Enter an item to be removed: ")
            for item in items:
                if item["task"] == info:
                    items.remove(item)
                    print(f"{item} deleted successfully") 
            else:
                print(f"{item} not found")
                
        elif decision == "3":
            print("available items: ")
            if not items:
                print("No item in the list")
            else:
                for item in items:
                    if item["completed"]:
                        print(f"✅ {item["item"]}")
                    else:
                        print(f"_ {item}")
                    
        elif decision == "4":
            edit = input("Enter what you want to replace: ")

            for item in items:
                if edit in items:
                    edited_item = input("Enter the correct item: ")
                    index = items.index(edit)
                    items[index] = edited_item
                    # items.insert(1,edit)
                    # items[item] = edit
                    # break
                else:
                    print("Item not found")
        elif decision == "5":
            task = input("Todo list: ")
            for item in items:
                if item ["task"] == task:
                    item["completed"] = True
                    print("item completed successfully")
                    break
                else:
                    print("item not found")

                
        elif decision == "6":
            break
        else:
            print("Invalid choice")
my_to_do_list()



