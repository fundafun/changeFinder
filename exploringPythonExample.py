'''
CALCULATE CHANGE

Week 1 - Module: Exploring Python, Example program

The goal of this program is to calculate the amount of change a customer 
should recieve based on the cost of their purchase and amount of money given 
to the cashier.  The user should input the total price and the amount given
to the cashier.  The output should inlcude the change due back to the customer
including all coin denominations (dollars, quarters, dimes, nickels, pennies)

1. Run the program several times, trying different input values.
   What happens if you enter 0 for received amount?

2. Under each 'ACTION ITEM' add a comment that describes the purpose
   of each line of code.

3. How could we write this program differntly?  How would that approach be better?

CHALLENGE OPTION:
Create the program from scratch and verify the user provides valid input, i.e. no negative numbers and no values that are less than total cost of purchase.
'''

# ACITON ITEM: What do the following 2 lines of code do? 
totalAmount = round(100 * float(input("Enter the total cost of the purchase: $")))
receivedAmount = round(100 * float(input("Enter the amount given to the cashier: $")))


# ACITON ITEM: What does the following line of code do? 
change = receivedAmount - totalAmount

print("Your change:")


# ACITON ITEM: What do the following 9 lines of code do?
dollars = int(change / 100)
change = change - (dollars * 100)  # ACTION ITEM: What is the purpose of this line?


quarters = int(change / 25)
change = change - (quarters * 25)

dimes = int(change / 10)
change = change - (dimes * 10)

nickels = int(change / 5)
change = change - (nickels * 5)

pennies = int(change / 1)


# ACITON ITEM: What does the following 5 lines of code do? 
print("   dollars       ",      dollars)
print("   quarters      ",     quarters)
print("   dimes         ",        dimes)
print("   nickels       ",      nickels)
print("   pennnies      ",     pennies)

