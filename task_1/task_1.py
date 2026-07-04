def main():
    my_tasks = []
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            my_tasks.append(task)
            print(f"'{task}' added!")
        elif choice == "2":
            if not my_tasks:
                print("No tasks yet!")
            else:
                for index, task in enumerate(my_tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
