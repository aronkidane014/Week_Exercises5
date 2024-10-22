
food_cost = 79.25
tax = 6.54
tip = 12.00

total_due = food_cost + tax + tip

#print("The total due is " + str(total_due))
# Q2 the str value is used for to join with "the total value is" in order to print them together the have to be the same type.

print("food cost is"+ str(food_cost) + "and tax is" + str(tax))
#print("Tip is" + str(total_due))
print("Total Due is" + str(total_due))
print("Tip is " + format(tip, ".2f"))