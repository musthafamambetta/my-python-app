import streamlit as st
import fcn

todos = fcn.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fcn.write_todos(todos)
    




st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("This app will increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fcn.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...:",
              on_change=add_todo, key="new_todo")