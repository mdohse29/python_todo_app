import time
import os

DEFAULT_FILE_PATH = 'todos.txt'


def get_todos(fp=DEFAULT_FILE_PATH):
    """ Retrieves the list of todos from the todos.txt file """
    # read_file = open("todos.txt", "r")
    # todo_list = read_file.readlines()
    # read_file.close()
    if not os.path.exists(fp):
        update_todos([], fp)

    with open(fp, 'r') as read_file:
        todo_list = read_file.readlines()

    if len(todo_list) <= 0:
        todo_list = []

    todo_list = [i.replace('\n', '') for i in todo_list]

    return todo_list


def update_todos(tdl: list, fp=DEFAULT_FILE_PATH):
    """ Takes in a List of todo items and updates the todos.txt file """
    # write_file = open("todos.txt", "w")
    # write_file.writelines(todo_list)
    # write_file.close()
    todo_list = tdl.copy()
    for index, item in enumerate(todo_list):
        if not item.endswith('\n') and item != '':
            todo_list[index] = item + '\n'
    with open(fp, 'w') as write_file:
        write_file.writelines(todo_list)


def show_todo_list():
    """ Prints out the list of todo items """
    todo_list = [print(f"{index + 1}) {item.strip().capitalize()}") for index, item in enumerate(get_todos())]
    if len(todo_list) <= 0:
        print("The todo list is empty")
    print()


def time_stamp():
    ts = time.strftime('%A - %b %d, %Y %H:%M:%S')
    return ts
