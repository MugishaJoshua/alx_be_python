# daily_reminder.py

# Prompt user for task details with exact wording
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Provide reminder directly in print using match-case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a HIGH priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a HIGH priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a MEDIUM priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a MEDIUM priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a LOW priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a LOW priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: '{task}' has an UNKNOWN priority level.")
