# daily_reminder.py

# Prompt user for task details with exact wording
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

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
else:
    reminder += ". Consider completing it when you have free time."

# Provide the customized reminder
print(reminder)
