# ╔══════════════════════════════════════╗
# ║     PROJECT: TO-DO LIST MANAGER      ║
# ╚══════════════════════════════════════╝

import json
import os

def load_tasks():                            # Function consisting file path
    if os.path.exists("main.json"):
        with open("main.json", "r") as f:
            return json.load(f)
    else:
        return {}
    
task= load_tasks()

def menu():                                     # Function consisting menu
    print("")
    print("─────────|Welcome to the Task Manager|─────────")
    print("")
    print("                  ❀ MENU ❀")
    print("───────────────────────────────────────────────")
    print("1> Add Task")
    print("2> View All Tasks")  
    print("3❯ Update Task")  
    print("4❯ Delete Task") 
    print("5❯ Exit")
    return

menu()

choice= input("Enter Choice from menu: ")        # Accept the input for choices for doing operations

while True:
    if choice== "1":                                                 # This loop lets you choose for Adding the task
        add= input("Enter the Serial no. of the Task: ")
        add1= input("Enter the Task: ")

        if add in task :                # This loop checks whether the task is in the list or not, if yes then else will execute or this loop ends with the message!
            print("Task with this Serial No. already exists. Please use a different Serial No.")
        else:                           # This else add the given task according to serial number
            with open("main.json", "w") as f:
                task[add]=[add1]
                task =json.loads(json.dumps(task))
                json.dump(task, f, indent=4)
        
                print("Task Added Successfully")
                

        menu()                                      # Menu Function
        choice= input("Enter Choice from menu: ")                   # Accept the input for choices for doing operations

        

    elif choice =="2":                                       # This loop lets you choose for Viewing all the task
        with open("main.json", "r") as f:
            task1= f.read()
            print("All Tasks are:" , task1)
                                                                                        
            if len(task) != 0:                                          # This loop givs the serial no. and task in a proper format.
                for serial_no, task in task.items():
                    print(f"Serial No: {serial_no}, Task: {task[0]}")
            else:
                print("No tasks found.")

            
        menu()                                          # Menu Function
        choice= input("Enter Choice from menu: ")               # Accept the input for choices for doing operations



    elif choice =="3":                                              # This loop lets you choose for Updating the existed task
        serialno= input("Enter the Serial No. of the Task to be Updated: ")
        task1 = input("Enter the Updated Task: ")

        if serialno not in task:           # This loop checks whether the task is in the list or not, if yes then else will execute or this loop ends with the message!
            print("Task with this Serial No. does not exist. Please check the Serial No.")
        else:                                       # This else Update task
            with open("main.json", "w") as f:
                task[serialno]=[task1]
                json.dump(task, f, indent=4)
                print("Task Updated Successfully")

        menu()                                      # Menu Function
        choice= input("Enter Choice from menu: ")       # Accept the input for choices for doing operations



    elif choice =="4":                                               # This loop lets you choose for Deleting the task
        serialno1= input("Enter the Serial no. of the Task to be Deleted: ")

        if serialno1 not in task:       # This loop checks whether the task is in the list or not, if yes then else will execute or this loop ends with the message!
            print("Task with this serial No. does not exist. Please check the Serial No.")
        else:                                                           # This else Deletes the task 
            with open("main.json", "w") as f:
                del task[serialno1]
                json.dump(task, f, indent=4)
                print("Task Deleted Successfully")

            menu()                                      # Menu Function
            choice= input("Enter Choice from menu: ")       # Accept the input for choices for doing operations



    elif choice =="5":                                              # This loop lets you Exit the Program
        print("Exiting the Task Manager. Goodbye!")
        break

    
    else:                                                           # This execute when you enter anything except(1,2,3,4 and 5) and ends the program with the message!
        print("Invalid choice. Please select a valid option from the menu.")
        break


            


        



