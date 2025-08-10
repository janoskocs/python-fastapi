from fastapi import FastAPI, HTTPException
from typing import List
from models import TodoItem

app = FastAPI()

todos = []
current_id = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to my todo app"}

@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    return todos

@app.post("/todos", response_model=TodoItem)
def create_todo(todo: TodoItem):
    global current_id
    todo.id = current_id
    current_id +=1
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, updated_todo: TodoItem):
    for idx, todo in enumerate(todos):
        if (todo.id == todo_id):
            todos[idx] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo doesn't exist.")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(idx)
            return {"details": "Todo deleted."}
    raise HTTPException(status_code=404, detail="Todo doesn't exist.")
