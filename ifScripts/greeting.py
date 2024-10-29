
def get_greeting(current_hour):
    """Return a greeting based on the current hour."""
    if 23 <= current_hour or current_hour < 5:
        return "What are you doing up so late??"
    elif current_hour < 10:
        return "Good morning!"
    elif 10 <= current_hour < 17:
        return "Good day!"
    else:
        return "Good evening!"

def main():
    current_hour = 0  
    greeting = get_greeting(current_hour) 
    print(greeting)

if __name__ == "__main__":
    main()
