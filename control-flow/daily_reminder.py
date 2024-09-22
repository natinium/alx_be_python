task = input("What do you want to do? ")
priority = input("What is the task's priority? (High/Medium/Low) ")
time_bound = input("Is the task time bounded? (Yes or No) ")

match priority:
    case "High":
        if time_bound == "Yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "Medium":
        if time_bound == "Yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case "Low":
        if time_bound == "Yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority")