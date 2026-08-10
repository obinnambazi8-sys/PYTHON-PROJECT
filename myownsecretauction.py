import os

def screen_wiper():
    if os.name =='nt':
        os.system("cls")
    else:
        os.system("clear")

# screen_wiper()


def highest_bidder(all_bidders):
    highest_bid = 0
    winner_bid = ''
    for bidder in all_bidders:
        bidamount = all_bidders[bidder]
        if bidamount > highest_bid:
            highest_bid = bidamount
            winner = bidder
    print(f"the winner of the highest bid is: {winner} with {highest_bid}")


def bidding_app():
    bidder = {}
    print("Your welcome to the secret auction. Make sure your bid is a decimal")
    continuous_bidding = True
    while continuous_bidding:
        name = input("What is your name? ")
        user_bid = float(input("What is your bid?:$"))
        bidder[name]= user_bid
        going_again=input("Are there any other bidders? Type 'yes' or 'no'? ")
        if going_again == 'no':
            continuous_bidding = False
            highest_bidder(bidder)
            break
        elif going_again =='yes':
            screen_wiper()

bidding_app()

