class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task

    def mark_done(self, title):
        task = self.find_task(title)
        if task:
            task.status = "Done"
        else:
            return "Task not found"

    def reopen_task(self, title):
        task = self.find_task(title)
        if task:
            task.status = "Todo"
        else:
            return "Task not found"

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                break

    def count_total(self):
        return len(self.tasks)

    def count_completed(self):
        done = 0
        for task in self.tasks:
            if task.status == "Done":
                done += 1
        return done

    def count_high_priority(self):
        high = 0
        for task in self.tasks:
            if task.priority == "High":
                high += 1
        return high


