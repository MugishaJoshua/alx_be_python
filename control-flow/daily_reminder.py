# daily_reminder.py

# Prompt user for task details
task = input("Enter the task: ").strip()
priority = input("Enter the task's priority (high/medium/low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# Process the task using match-case
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task"
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority level"

# Modify the reminder based on time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder += ". Time-bound input was invalid."

# Provide the customized reminder
print(reminder)
