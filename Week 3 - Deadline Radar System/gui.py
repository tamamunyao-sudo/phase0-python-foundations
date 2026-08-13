import tkinter as tk
import task as task
import database as db
import task_manager as tm

window = tk.Tk()
window.title("Deadline Radar Project")
window.geometry("700x500")

frame = tk.Frame(window)
frame.pack()

title_label = tk.Label(frame, text="Title")
title_label.grid(row=0, column=0)

category_label = tk.Label(frame, text="Category")
category_label.grid(row=1, column=0)

due_date_label = tk.Label(frame, text="Due Date")
due_date_label.grid(row=2, column=0)

priority_label = tk.Label(frame, text="Priority")
priority_label.grid(row=3, column=0)

status_label = tk.Label(frame, text="Status")
status_label.grid(row=4, column=0)

title_entry = tk.Entry(frame)
category_entry = tk.Entry(frame)
due_date_entry = tk.Entry(frame)
priority_entry = tk.Entry(frame)
status_entry = tk.Entry(frame)

title_entry.grid(row=0, column=1)
category_entry.grid(row=1, column=1)
due_date_entry.grid(row=2, column=1)
priority_entry.grid(row=3, column=1)
status_entry.grid(row=4, column=1)

status_message_label = tk.Label(frame, text="Status")
status_message_label.grid(row=5, column=0)

task_board = tk.Listbox(frame, width=30, height=10)
task_board.grid(row=8, column=0, columnspan=2)

total_tasks_label = tk.Label(frame, text="Total Tasks")
total_tasks_label.grid(row=1, column=5)

completed_tasks_label = tk.Label(frame, text="Completed Tasks")
completed_tasks_label.grid(row=2, column=5)

high_priority_label = tk.Label(frame, text="High Priority")
high_priority_label.grid(row=3, column=5)

manager = tm.TaskManager()

def load_into_manager():
    rows = db.load_tasks()

    for row in rows:
        title = row[0]
        category = row[1]
        due_date = row[2]
        priority = row[3]
        status = row[4]

        task_obj = task.Task(title, category, due_date, priority, status)
        manager.add_task(task_obj)

def dashboard_update():

    total = manager.count_total()
    done = manager.count_completed()
    high = manager.count_high_priority()

    total_tasks_label.config(text=f"Total Tasks: {total}")
    completed_tasks_label.config(text=f"Completed Tasks: {done}")
    high_priority_label.config(text=f"High Priority: {high}")

def load_tasks():
    task_board.delete(0, tk.END)

    tasks = manager.list_tasks()

    for task in tasks:
        title = task.title
        category = task.category
        due_date = task.due_date
        priority = task.priority
        status = task.status

        string = f"{title} | {category} | {due_date} | {priority} | {status}"

        task_board.insert(tk.END, string)

def save_tasks():

    title = title_entry.get().strip()
    category = category_entry.get().strip()
    due_date = due_date_entry.get().strip()
    priority = priority_entry.get().strip()
    status = status_entry.get().strip()

    if not title or not category or not due_date or not priority or not status:
        status_message_label.config(text="Please Enter the required fields")
        return
    else:
        task_object = task.Task(title, category, due_date, priority, status)
        manager.add_task(task_object)
        db.save_task(task_object)

        title_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)
        status_entry.delete(0, tk.END)

    load_tasks()
    dashboard_update()

save_task_button = tk.Button(frame, text="Save Task", command=save_tasks)
save_task_button.grid(row=6, columnspan=2)

load_into_manager()
load_tasks()
dashboard_update()

def run_window():
    window.mainloop()
