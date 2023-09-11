import tkinter as tk
from tkinter import messagebox
from datetime import datetime
root = tk.Tk()
root.title("To-Do List Application")
tasks = []
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_listbox()
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()
listbox = tk.Listbox(root, width=40, selectmode=tk.SINGLE)
listbox.pack()
def remind():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messagebox.showinfo("Reminder", f"Don't forget your tasks! Current time: {current_time}")
reminder_button = tk.Button(root, text="Set Reminder", command=remind)
reminder_button.pack()
root.mainloop()
