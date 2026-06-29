# ╔══════════════════════════════════════╗
# ║     PROJECT: TO-DO LIST MANAGER      ║
# ╚══════════════════════════════════════╝

import json

task={}

def menu():
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
        with open("main.json", "w") as f:
            task[serialno]=[task1]
            task2= f.write(str(task))
            print("Task Updated Successfully")

        menu()
        choice= input("Enter Choice from menu: ")
        



