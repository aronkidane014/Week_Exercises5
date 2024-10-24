import math
X=38
number_of_vans= math.ceil(X/15)
total_cost= number_of_vans * 250
cost_per_person= total_cost/X
print(format(total_cost, ".1f")) #cost of van for question 6C

print(cost_per_person, ".1f") #charge per person for question 6A

print(X * total_cost) #the total money collected for question 6B
# there is leftover money because the number of people doesn’t divide evenly into the total cost.