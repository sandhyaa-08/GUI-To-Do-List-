import tkinter as tk
from tkinter import messagebox
import pandas as pd

FILE = "tasks.csv"

def load_tasks():
    try:
        df = pd.read_csv(FILE)
        for task in df["Task"]:
            listbox.insert(tk.END, task)
    except:
        pass

def save_tasks():
    tasks = listbox.get(0, tk.END)
    df = pd.DataFrame(tasks, columns=["Task"])
    df.to_csv(FILE, index=False)

def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Enter a task!")
    else:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task!")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(tk.END, "✔ " + task)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task!")

root = tk.Tk()
root.title("Todo List")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="#2f3640")

tk.Label(root, text="📝 My Todo List", font=("Arial", 16, "bold"),bg="#2f3640", fg="white").grid(row=0, column=0, columnspan=3, pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

tk.Button(root, text="Add", command=add_task,bg="#44bd32", fg="white").grid(row=2, column=1, sticky="ew")

tk.Button(root, text="Delete", command=delete_task,bg="#e84118", fg="white").grid(row=3, column=1, sticky="ew")

tk.Button(root, text="Done", command=mark_done,bg="#00a8ff", fg="white").grid(row=4, column=1, sticky="ew")

listbox = tk.Listbox(root, font=("Arial", 12))
listbox.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="nsew")

root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure((0,1,2), weight=1)

load_tasks()
root.mainloop()
