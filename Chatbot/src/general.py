import os

DATA_DIR = "data"

def get_user_filepath(username, filetype):
    """Constructs a user-specific filepath inside the data directory."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    return os.path.join(DATA_DIR, f"{username}_{filetype}.txt")

def load_tasks(username):
    """Loads tasks for a specific user from their file."""
    filepath = get_user_filepath(username, "tasks")
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(username, tasks):
    """Saves tasks for a specific user to their file."""
    filepath = get_user_filepath(username, "tasks")
    with open(filepath, "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

def general(name):
    tasks = load_tasks(name)
    notes_filepath = get_user_filepath(name, "notes")

    while True:
            print(f"How can I help you {name}?") 
            
            print("\n1-Help you manage your tasks")
            print("2-Notes app")
            print("Press X to return to the main menu")
            print("")

            opt = input("")

            if opt.lower() == "x": # This was opt == 2 before, now it's the main task manager menu
                break
            
            if opt == "1":
                
                while True:

                    print("\n1-See your tasks ")
                    print("2-Add tasks")
                    print("3-Remove tasks")
                    print("4-Edit tasks")
                    print("press X to exit To Do list")

                    opt = input("") # This is the inner option for the to-do list

                    if opt == "1":
                    
                        if tasks == []:
                            print("No tasks yet")
                            continue
                        else:
                            print(tasks)
                            continue    
                    
                    if opt == "2":
                        task = input("What is the task you want to add?: ")
                        tasks.append(task)
                        save_tasks(name, tasks)
                        print(task," has been added to your to do list")
                        continue
                    
                    if opt == "3":
                        if not tasks:
                            print("No tasks to remove.")
                            continue
                        remove = input("What task do you want to remove?: ")
                        if remove not in tasks: # Corrected spelling from 'exsist'
                            print("This task does not exsist")
                            continue

                        tasks.remove(remove)

                        print(remove," has been removed from To Do list")
                        continue
                        
                    if opt == "4":
                        if not tasks:
                            print("No tasks to edit.")
                            continue
                            
                        old_task = input("Which task do you want to edit?: ")
                        
                        if old_task not in tasks:
                            print("This task does not exist.")
                            continue
                        
                        new_task_name = input(f"What should '{old_task}' be changed to?: ")
                        try:
                            task_index = tasks.index(old_task)
                            tasks[task_index] = new_task_name
                            save_tasks(name, tasks)
                            print(f"Task '{old_task}' has been updated to '{new_task_name}'.")
                        except ValueError:
                            # This case is unlikely due to the 'in' check, but it's good practice
                            print("Could not find the task to edit.")
                        continue

                    if opt.lower() == "x":
                        break

            # This should be option 2 for the notes app
            if opt == "2":
                while True:
                    print("\n\n1-Add note\n2-See your notes\nPress x to exit")

                    ch1 = input("\n")
                    
                    if ch1 == "1":
                        with open(notes_filepath, "a") as notes_file:
                            added_note = input("\nNote: ")
                            notes_file.write(f"{added_note}\n")
                        print("Note added.")

                    elif ch1 == "2":
                        try:
                            with open(notes_filepath, "r") as notes_file:
                                print("\n--- Your Notes ---")
                                print(notes_file.read())
                                print("------------------")
                        except FileNotFoundError:
                            print("You don't have any notes yet.")

                    elif ch1.upper() == "X":
                        break
