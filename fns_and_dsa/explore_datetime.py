# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days_to_add):
    """
    Calculate and display the date after adding a given number of days
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
