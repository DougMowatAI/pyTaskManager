class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
    
    def update_Title(self, new_title):
        self.title = new_title
    
    def mark_Complete(self):
        complete = True
    
    def delete(self):
        delete = True