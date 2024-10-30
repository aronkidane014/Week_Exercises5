# hours_worked= float(input("hours worked: "))
# pay_rate= float(input("Pay Rate: "))
# if hours_worked > 40:
#     regular_pay= hours_worked * 40,
#     overtime= (hours_worked - 40) * 1.5,
#     total_pay= regular_pay + overtime

# else:
#    total_pay= hours_worked * pay_rate
# print(f"your pay check is {total_pay}")
     
hours_worked = float(input("Hours worked: "))
pay_rate = float(input("Pay Rate: "))

if hours_worked > 40:
    regular_pay = 40 * pay_rate  
    overtime = (hours_worked - 40) * pay_rate * 1.5 
    total_pay = regular_pay + overtime
    print(f"You worked extra, more money for you! Total pay: ${total_pay:.2f}")
elif hours_worked < 40:
    total_pay = hours_worked * pay_rate
    print(f"Your paycheck is lower due to fewer hours. Total pay: ${total_pay:.2f}")
elif hours_worked == 40:
    total_pay = hours_worked * pay_rate
    print(f"You worked the standard 40 hours. Total pay: ${total_pay:.2f}")




     