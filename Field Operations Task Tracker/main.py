import argparse
from logic import *




#Creating an ArgumentParser Object
parser = argparse.ArgumentParser(prog = 'Field Operations Task Tracker',description= "Used to track field tasks",epilog="Thank you for using %(prog)s")

#Creating a subparser object
sub_parser = parser.add_subparsers(title="subcommands",description='Actions that you can perform with the app',
                                   help='add,view and filter tasks')

#Creating arguments to come after the subparser 'add' for when the user wants to add an expense
add_task_parser = sub_parser.add_parser('add',help='add a task')
add_task_parser.add_argument('name',help = 'The task name',type=str)
add_task_parser.add_argument('--status',default='Pending',help='The completion status of the task',choices=['Pending','Ongoing','Completed'])
add_task_parser.add_argument('--assigned',default='Unassigned',help='The person assigned to the task',type=str)
add_task_parser.add_argument('--site',default='Unknown Site',help='The site of the task',type=str)
add_task_parser.add_argument('--priority',default='Medium',help='The priority of the task',choices=['High','Medium','Low'])
add_task_parser.add_argument('--due',default="NIL",help="The task's due date",type=str)
add_task_parser.add_argument('--notes',default="No notes",help="Notes about or description of the task",type=str)
#Linking the add_task() function to the add command
add_task_parser.set_defaults(func=add_task)

#Creating the view subparser
view_tasks_parser = sub_parser.add_parser('view',help='View a list of saved tasks',description='View your tasks')
view_tasks_parser.set_defaults(func=view_tasks)


#Creating a filter parser from the view subparser created
filter_tasks_parser = sub_parser.add_parser('filter',help='view tasks based on a filter')
filter_tasks_parser.add_argument('--status',help='Filter by completion status of the task',choices=['Pending','Ongoing','Completed'])
filter_tasks_parser.add_argument('--priority',help='filter by the priority of the task',choices=['High','Medium','Low'])
filter_tasks_parser.set_defaults(func=filter_tasks)


args = parser.parse_args()
arguments = vars(args).copy()
arguments.pop('func', None)
args.func(arguments)











