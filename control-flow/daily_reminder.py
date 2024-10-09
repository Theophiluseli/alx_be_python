# daily_reminder.py

# Prompt for a single task
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes/no): ").lower()

# Initialize the reminder message
reminder = f"Reminder: You have a task - '{task}' with priority '{priority}'"

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder += " that requires immediate attention today!"
    case "medium":
        reminder += " - please try to complete it soon."
    case "low":
        reminder += " - it can be addressed later."
    case _:
        reminder += " - priority not recognized."

# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder = f"Attention! {reminder} Make sure to prioritize it today!"

# Provide a customized reminder
print(reminder)
