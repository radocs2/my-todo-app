import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    n_todo = st.session_state["new_todo"] + "\n"
    todos.append(n_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
