# daily_reminder.py

while True:
    # Prompt user for task details
    task = input("Enter the task: ")
    priority = input("Enter the task's priority (high/medium/low): ").lower()
    time_bound = input("Is the task time-bound? (yes/no): ").lower()

    # Process the task using match case
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a HIGH priority task."
        case "medium":
            reminder = f"Reminder: '{task}' is a MEDIUM priority task."
        case "low":
            reminder = f"Reminder: '{task}' is a LOW priority task."
        case _:
            reminder = f"Reminder: '{task}' has an UNKNOWN priority level."

    # Add time sensitivity
    if time_bound == "yes":
        reminder += " This requires immediate attention today!"

    # Output the reminder
    print(reminder)

    # Ask if the user wants to enter another task
    again = input("Do you want to add another task? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye! Stay productive.")
        break
