import database
from task_logic import display_Options, get_Choice, verify_Choice, add_new_task

def main():
    #Set Program to Active
    Active = True
    database.create_table()

    while Active:
        #Display Options to User
        display_Options()

        choice = get_Choice()

        if verify_Choice(choice):

            if choice == "1":
                add_new_task()

            elif choice == "2":
                print("Editing Task")

            elif choice == "3":
                print("Deleting Task")

            elif choice == "4":
                print("Viewing All Tasks")           
            
            else:
                print("Goodbye!")
                Active = False
        else:
            print("Invalid Selection, please select a valid option between 1-5")

if __name__ == "__main__":
    main()