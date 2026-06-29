# 📋 Simple To-Do List Manager

This is a text-based To-Do List application built with Python. I created this project to practice working with Python dictionaries, menus, and saving data into JSON files. ✨

## 🚀 What it Does

* **➕ Add Task**: Saves a new task using a custom Serial Number. It checks to make sure you do not use a duplicate number.
* **👁️ View Tasks**: Reads the file and prints all your current tasks on the screen.
* **✏️ Update Task**: Edits the text of a task you already created.
* **❌ Delete Task**: Removes a task from the list using its Serial Number.
* **🚪 Exit**: Safely closes the application.

## 💾 How the Data Saves

The program automatically creates a file named `main.json` in the same folder to store your text. It organizes the data like this:

```json
{
    "1": [
        "i have to code for 4 hrs"
    ],
    "2": [
        "And push it on Github"
    ]
}
```

### 🧠 Understanding the File Structure:
* The `"1"` or `"2"` outside the brackets is the **Serial Number** of the task.
* The text inside the brackets is the actual **Task** description.

## 💻 How to Run the Project

1. Download the `TO-DO_main.py` file to your computer.
2. Open your terminal or command prompt in that folder.
3. Run the script by typing:
   ```bash
   python TO-DO_main.py
   ```

---

## 🛠️ Project Status & Future Plans
The initial core features of this project are finished and working! However, it is not completely done yet. I plan to upgrade it and add more advanced features in the future as I learn more Python. 🚀
