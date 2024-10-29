# Assign values to variables a, b, and c
a = 10
b = 25
c = 15

# Determine the smallest number
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Determine the largest number
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Display the results
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")
