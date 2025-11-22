import json
import ast
from prettytable import PrettyTable

main_table = PrettyTable()

def add_task(dict):
    """This function lets the user adds a task that would then be apended to a log file"""
    with open("tasks.jsonl",'a') as file:
        json.dump(dict,file)
        file.write("\n")

def view_tasks(Dummy):
    """This function displays the table."""
    print(table())

def table():
    """This function converts the data into an ascii table and returns it."""
    tasks=[]
    with open("tasks.jsonl", "r") as file:
            for line in file:
                data = ast.literal_eval(line)
                tasks.append(data)
    main_table.field_names = tasks[0].keys()
    for row in tasks:
        main_table.add_row(row.values())
    return main_table

def filter_tasks(dict):
    """This function only displays tasks that meet a certain criteria"""
    if dict['status'] is None:
        if dict['priority'] is None:
            print("Select a criteria")
        else:
            print(table().get_string(row_filter=make_filter_priority(dict['priority'])))
    else:
        print(table().get_string(row_filter=make_filter_status(dict['status'])))
 
def make_filter_status(criteria):
    """This function filters the table based on the pstatus"""
    def filter_function(row):
        return row[1] == criteria
    return filter_function

def make_filter_priority(criteria):
    """This function filters the table based on thetask's priority"""
    def filter_function(row):
        return row[4] == criteria
    return filter_function
