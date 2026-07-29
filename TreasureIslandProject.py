print("Welcome to Treasure Island. Your mission is to find the treasure.")
location=input("You are at a cross road. Where do you want to go Type 'left' or 'right'?  ")


if location == 'left':
    print("You have come to a lake. There is an island in the middle of the lake.")

    decision=input("Type 'wait' to wait for a boat.Or type 'swim' to swim across. ")
    if decision == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. ")


        door_color= input("red,yellow and blue. Which color do you choose? ")
        if door_color == "red":
            print("Its a room full of fire. Game Over.")
        elif door_color == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over. ")
else:
    print("You fell into a hole. Game Over. ")
