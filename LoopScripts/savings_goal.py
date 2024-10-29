starting_balance = 1000  
savings_goal = 5000     
weekly_savings = 200      

current_balance = starting_balance

while current_balance < savings_goal:
    current_balance += weekly_savings
    print(f"This week my balance increased to {current_balance}.")

    if current_balance > savings_goal / 2:
        print(f"Almost there! This week my balance is up to {current_balance}.")
    
    if current_balance >= savings_goal * 0.75:
        treat_amount = 100
        current_balance -= treat_amount
        print(f"So close! After treating myself, my balance is up to {current_balance}.")

print(f"Goal met! My current balance is {current_balance}.")
