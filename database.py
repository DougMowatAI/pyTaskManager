import sqlite3



def create_table():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    description TEXT,
                    due_date TEXT
                )''')

    conn.commit()
    conn.close()

def insert_task(task):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    
    c.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)",
              (task.title, task.description, task.due_date))
    
    conn.commit()
    conn.close()
    