def task():
    tasks = [] #empty list
    print("-----Welcome to task Management App------")


    total_task = int(input("Enter how many task you want to add: "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} :")
        tasks.append(task_name) 
    
    print(f"Today's task are\n {tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1:
            add = input ("Enter task you want to add: ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")
        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter new task:")
                ind = tasks.index(updated_val)
                tasks[ind] = up #Update
                print(f"Updated Task are\n {tasks}")

        elif operation == 3:
            delete_val = input("Enter the task name you want to Delete: ")
            if delete_val in tasks:
                ind = tasks.index(delete_val)
                del tasks[ind]
                print(f"Item deleted successfuly\n {tasks}")

        elif operation == 4:
            print(f"Your todo list:\n {tasks}")
        elif operation == 5:
            break
        else:
            print("Invalid Code kindly enter proper code!")
task()