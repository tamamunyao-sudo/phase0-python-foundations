class Task:
    def __init__(self, title, category, due_date, priority, status):
        self.title = title
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"{self.title} | {self.category} | {self.due_date} | {self.priority} | {self.status}"

