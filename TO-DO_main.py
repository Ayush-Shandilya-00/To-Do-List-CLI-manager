# ╔══════════════════════════════════════╗
# ║     PROJECT: TO-DO LIST MANAGER      ║
# ╚══════════════════════════════════════╝

import json
import os

def load_tasks():
    if os.path.exists("main.json"):
        with open("main.json", "r") as f:
            return json.load(f)
    else:
        return {}
    
task= load_tasks()

def menu():
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

choice= input("Enter Choice from menu: ")

while True:
    if choice== "1":
        add= input("Enter the Serial no. of the Task: ")
        add1= input("Enter the Task: ")
        if add in task :
            print("Task with this Serial No. already exists. Please use a different Serial No.")
            
        else:

            with open("main.json", "w") as f:
                task[add]=[add1]
                task =json.loads(json.dumps(task))
                json.dump(task, f, indent=4)
        
                print("Task Added Successfully")
                

        menu()
        choice= input("Enter Choice from menu: ")

        

    elif choice =="2":
        with open("main.json", "r") as f:
            task1= f.read()
            print("All Tasks are:" , task1)
            

        menu()
        choice= input("Enter Choice from menu: ")

    elif choice =="3":
        serialno= input("Enter the Serial No. of the Task to be Updated: ")
        task1 = input("Enter the Updated Task: ")
        if serialno not in task:
            print("Task with this Serial No. does not exist. Please check the Serial No.")
            
        else:

            with open("main.json", "w") as f:
                task[serialno]=[task1]
                json.dump(task, f, indent=4)
                print("Task Updated Successfully")

        menu()
        choice= input("Enter Choice from menu: ")

    elif choice =="4":
        serialno1= input("Enter the Serial no. of the Task to be Deleted: ")

        if serialno1 not in task:
            print("Task with this serial No. does not exist. Please check the Serial No.")
        else:
            with open("main.json", "w") as f:
                del task[serialno1]
                json.dump(task, f, indent=4)
                print("Task Deleted Successfully")

            menu()
            choice= input("Enter Choice from menu: ")

    elif choice =="5":
        print("Exiting the Task Manager. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option from the menu.")
        break


            


        



