import tkinter as tkinter
from tkinter import messagebox

tasks = []


def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tkinter.END, task)
        entry.delete(0, tkinter.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        tasks.pop(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")


root = tkinter.Tk()
root.title("To-Do List")
root.geometry("400x400")

entry = tkinter.Entry(root, width=30)
entry.pack(pady=10)

tkinter.Button(root, text="Add Task", command=add_task).pack()

listbox = tkinter.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

tkinter.Button(root, text="Delete Task", command=delete_task).pack()

root.mainloop()

