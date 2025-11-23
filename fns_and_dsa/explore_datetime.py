from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    # Format it
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # return for later use if needed

def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.now()
    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)
    # Format and print
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Get user input and calculate future date
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)

if __name__ == "__main__":
    main()
