task = input("Enter your task: ")
priority = input("What is the task's priority? (high/medium/low) ")
time_bound = input("Is it time-bound? yes/no ")

match priority:
    case "high":
        if time_bound == "Yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "Yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "Yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority")