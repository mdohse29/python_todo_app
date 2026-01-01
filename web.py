import streamlit as sl
import todo_functions as todo_func

todos = todo_func.get_todos()


def add_todo():
    u_text = sl.session_state['u_input']
    sl.session_state['u_input'] = ''
    if todos.count(u_text) == 0:
        todos.append(u_text.strip())
        todo_func.update_todos(todos)


# def complete_todo():
#     for k, i in sl.session_state.items():
#         if i and k != 'u_input':
#             todos.pop(int(k))
#             todo_func.update_todos(todos)
#             break


# print('----NEW-----')
sl.title('My Todo App', text_alignment='center')
sl.subheader('Python Master Course: Todo Web App', text_alignment='center', divider='grey')
sl.write('TODO LIST:')

for n, td in enumerate(todos):
    # sl.checkbox(td, key=f"{n}", on_change=complete_todo)
    # my original way before watching the video ^^^^^^^^
    cb = sl.checkbox(td, key=f"{n}")
    if cb:
        todos.pop(n)
        todo_func.update_todos(todos)
        del sl.session_state[f"{n}"]
        sl.rerun()


sl.text_input(label="Enter a new todo", label_visibility='hidden', key="u_input", placeholder="Enter a new todo", on_change=add_todo)
