def task():
    tasks = []
    print("")
    print("___WELCOME TO DO LIST___")

    total_task = int(input("Enter how many tasks you want to add:= "))

    for i in range(1, total_task+1):
        task_name = input(f"Enter Task {i}= ")
        tasks.append(task_name)

    print("____YOUR TASKS____")
    for j in range(0, len(tasks)):
        print(f"{j+1}--{tasks[j]}")

    print("")
    while True:
        operation = int(input("Enter what you want:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit... "))
        if operation == 1:
            add = input("Enter task that you want to add= ")
            tasks.append(add)
            print(f"Task: {add} has been added... ")
            print("")


        elif operation == 2:
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task= ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task: {up}")
            print("")

        elif operation == 3:
            del_val = input("Which task you want to delete: ")

            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted..")
            print("")

        elif operation == 4:
            print("____YOUR TASKS____")
            for j in range(0, len(tasks)):
                print(f"{j + 1}--{tasks[j]}")
            print("")

        elif operation == 5:
            print("Closing the program :) ... ")
            break


task()