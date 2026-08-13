import sqlite3

def create_table():
    connection = sqlite3.connect("deadline_radar.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks(
        title TEXT,
        category TEXT,
        due_date TEXT,
        priority TEXT,
        status TEXT
        )
        """
    )

    connection.commit()
    connection.close()

def save_task(task):
    create_table()

    connection = sqlite3.connect("deadline_radar.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO tasks (title, category, due_date, priority, status) VALUES (?,?,?,?,?)",
                   (task.title, task.category, task.due_date, task.priority, task.status)
                   )

    connection.commit()
    connection.close()


def load_tasks():
    create_table()

    connection = sqlite3.connect("deadline_radar.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    connection.close()

    return tasks


