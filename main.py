# To Do List GUI application using Tkinter
from tkinter import *

GREEN = "#A1CCD1"
ORANGE = "#E9B384"

tasks = []


# ------------------------ ADD TASK ------------------------ #

def add_task():
    task_input = task_entry.get()
    tasks.append(task_input)
    listbox.insert(END, task_input)
    task_entry.delete(0, END)


# ------------------------ DELETE TASK --------------------- #

def remove_task():
    selected_item = listbox.curselection()
    listbox.delete(selected_item)
    element_index = int(''.join(map(str, selected_item)))
    tasks.pop(element_index)


# ------------------------ SAVE LIST ------------------- #

def save_list():
    with open("list.txt", mode="w") as file:
        for item in tasks:
            file.write(f"{item}\n")


# ------------------------ GUI SET UP ---------------------- #

# Window
window = Tk()
window.title("ToDo List")
window.config(padx=20, pady=20, bg=GREEN)

# Entry Label
entry_label = Label(text="Enter Your Task", bg=GREEN)
entry_label.grid(row=0, column=1)

# Task Entry
task_entry = Entry(width=30)
task_entry.grid(row=1, column=1)

# Add Button
add_button = Button(text="Add", bg=ORANGE, command=add_task)
add_button.grid(row=1, column=2)

# List Label
list_label = Label(text="Your List", bg=GREEN)
list_label.grid(row=2, column=1)

# Listbox
listbox = Listbox(height=10)
listbox.grid(row=3, column=1)

# Remove Button
remove_button = Button(text="Remove", bg=ORANGE, command=remove_task)
remove_button.grid(row=4, column=0)

# Save List Button
save_button = Button(text="Save List", bg=ORANGE, command=save_list)
save_button.grid(row=4, column=2)

window.mainloop()
