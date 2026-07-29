print("Welcome to the tip calculator!")
bill= int(input("what was the total bill? $ "))
# print(bill)
tip=int(input("How much tip would you like to give 10, 12, 15? "))
# print(tip)
people= int(input("How many people to split the bill? "))
# print(people)
tip_amount = bill*(tip / 100) 
total_tip = bill + tip_amount
Amount_per_person = total_tip / people
print(f"Each person should pay: ${Amount_per_person} ")
