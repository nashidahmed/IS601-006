from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")

    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    # nn379 6 Feb 2023
    # Check if all the fields are entered. If they are not, inform the user and exit the function, if they are, then:
    # 1. Assign lastActivity to the current time.
    # 2. Set the name, description and due date.
    # 3. Before setting the due date, check if the value entered is of a valid date format, else exit the function.
    # 4. Add the new task to the tasks list.
    if name and description and due:
        task['lastActivity'] = datetime.now()
        task['name'], task['description'] = name, description
        try:
            task['due'] = str_to_datetime(due)
        except:
            print('Invalid date format entered. Task not added. Try again.')
            return
        tasks.append(task)
        print('New task added!')
    else:
        if not name: print('No name given.', end=' ')
        if not description: print('No description given.', end=' ')
        if not due: print('No due date given.', end=' ')
        print('Task not added.')
        return

    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # nn379 7 Feb 2023
    # Check if the index exists in the tasks list, if so, request the user for the name, description and due date and call update_task, else inform the user that the task does not exist
    if 0 <= index < len(tasks):
        task = tasks[index]
        name = input(f"What's the name of this task? ({task['name']}) \n").strip()
        desc = input(f"What's a brief descriptions of this task? ({task['description']}) \n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S) ({task['due']}) \n").strip()
        update_task(index, name=name, description=desc, due=due)
    else:
        print('Task does not exist.')

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # nn379 7 Feb 2023
    # Get a valid task from the tasks list and check if the user has entered any values. If they have not, inform the user that the task has not been updated. If they have then:
    # 1. Assign lastActivity to the current time.
    # 2. Update the name, description or due date if they have been entered by the user, else keep the existing values
    # 3. Before setting the due date, check if the value entered is of a valid date format.
    # 4. Update the task and inform the user.
    task = {}
    if 0 <= index < len(tasks):
        task = tasks[index]
    else:
        print('Task does not exist.')
        return

    if name or description or due:
        try:
            task['due'] = due and str_to_datetime(due) or task['due']
        except:
            print('Invalid date format entered. Task not updated. Try again.')
            return
        task['lastActivity'] = datetime.now()
        task['name'], task['description'] = name or task['name'], description or task['description']
        print('Task updated successfully!')
    else:
        print('No input entered. Task not updated.')
        return
    
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # nn379 7 Feb 2023
    # Get a valid task from the tasks list and check if it is done, if it is not done, set the current datetime to the 'done' else inform the user that the task is already completed.
    task = {}
    if 0 <= index < len(tasks):
        task = tasks[index]
    else:
        print('Task does not exist.')
        return
    
    if not task['done']:
        task['done'] = datetime.now()
        print(f'Task {index + 1} marked as done.')
    else:
        print('Task already completed.')
        return
    
    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    # nn379 6 Feb 2023
    # Get a valid task from the tasks list and print the details of the task.
    task = {}
    if 0 <= index < len(tasks):
        task = tasks[index]
    else:
        print('Task does not exist.')
        return
    
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # nn379 7 Feb 2023
    # Get a valid task from the tasks list and delete the task by popping it from the tasks list.
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print('Task deleted successfully!')
    else:
        print('Task does not exist.')

    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # nn379 7 Feb 2023
    # Get the incomplete tasks from the tasks list by filtering out the tasks which have 'done' as false using list comprehension
    _tasks = [task for task in tasks if not task['done']]
    list_tasks(_tasks)

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # nn379 7 Feb 2023
    # Get the overdue tasks from the tasks list by filtering out the tasks that have 'due' before the current time and 'done' as false using list comprehension 
    _tasks = [task for task in tasks if str_to_datetime(str(task['due'])) < datetime.now() and not task['done']]
    list_tasks(_tasks)

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # nn379 7 Feb 2023
    # 1. Get a valid task from the tasks list
    # 2. Convert the 'due' time to datetime format and get the unformatted remainining time by simply finding the difference between the 'due' time and current time. Check which is later and use that as the first value when finding the difference.
    # 3. Compute the days, hours, minutes and seconds from the remaining time.
    # 4. Produce the string for days, hours, minutes and seconds separately accounting for plural if days, minutes, hours or seconds are more than one. If they are equal to 0, they are given empty string as value so they can filtered out in the next step. 
    # 5. Use join and filter out the empty strings to get a clean output for the days, hours, mintues and seconds.
    # 6. Check if the task is due or overdue and print out the remaining time accordingly.
    task = {}
    if 0 <= index < len(tasks):
        task = tasks[index]
    else:
        print('Task does not exist.')
        return

    now = datetime.now()
    due = str_to_datetime(str(task['due']))
    remaining_time = due - now if due > now else now - due

    days = remaining_time.days
    hours = remaining_time.seconds // 3600
    minutes = (remaining_time.seconds//60) % 60
    seconds = remaining_time.seconds % 60

    days_str = (f'{days} day' if days == 1 else f'{days} days') if days > 0 else ''
    hours_str = (f'{hours} hour' if hours == 1 else f'{hours} hours') if hours > 0 else ''
    minutes_str = (f'{minutes} minute' if minutes == 1 else f'{minutes} minutes') if minutes > 0 else ''
    seconds_str = (f'{seconds} second' if seconds == 1 else f'{seconds} seconds') if seconds > 0 else ''

    remaining_time_list = [days_str, hours_str, minutes_str, seconds_str]
    remaining_time_str = ', '.join(filter(None, remaining_time_list))

    if due > now:
        print(f'This task is due in {remaining_time_str}.')
    else:
        print(f'The task is overdue by {remaining_time_str}.')

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()
