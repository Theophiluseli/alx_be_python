# Importing necessary components from the datetime module
from datetime import datetime, timedelta

# Part 1: Function to display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format the date and time in "YYYY-MM-DD HH:MM:SS" format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted current date and time
    print(f"Current date and time: {formatted_date}")

# Part 2: Function to calculate a future date
def calculate_future_date(days):
    # Get the current date
    current_date = datetime.now().date()

    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days)
