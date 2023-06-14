import database
from models import Task

# Option Display for the User
def display_Options():
    print("##################### \n 1. Add a New Task \n 2. Edit Task \n 3. Delete Task \n ------------- \n 4. View All Tasks \n 5. Exit\n #####################")

# Get Option Selection from the User
def get_Choice():
    choice = input("Please Select An Option ")
    return choice

# Function to Verify what the user inputted is a valid choice
def verify_Choice(choice):
    valid_choices = ["1", "2", "3", "4", "5"]
    return choice in valid_choices

def add_new_task():
    title = input("Enter Task Title: ")
    description = input("Enter Task Description: ")
    due_date = input("Enter the desk due date (DD/MM): ")

    submit_Task = Task(title, description, due_date)
    database.insert_task(submit_Task)
    print("Task Added!")