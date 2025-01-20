"""main file for the app"""

from fastapi import FastAPI
from models import Todo
  
app = FastAPI()

@app.get("/")
async def root():
  """basic hello world"""
  return {"message": "Hello World"}

todos = [
  { "id": 1, "title": "Buy groceries", "completed": False },
  { "id": 2, "title": "Walk the dog", "completed": True }
]

# Get all todos
@app.get("/todos")
async def get_todos():
  """Get all todos"""
  return { "todos": todos }

# Get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
  """Get a single todo"""
  for todo in todos:
    if todo["id"] == todo_id:
      return { "todo": todo }

  return { "message": "No todo found for the corresponding ID" }

# Creata todo
@app.post("/todos")
async def create_todo(todo: Todo):
  """Create a todo"""
  todos.append(todo)
  return { "todo": todo }

# Update todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, updated_todo: Todo):
  """Update a todo"""
  for todo in todos:
    if todo["id"] == todo_id:
      todo.id = todo_id
      todo.title = updated_todo.title
      todo.completed = updated_todo.completed
      return { "updated todo": todo }

  return { "message": "No todo found for the corresponding ID to update" }

# Delete todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
  """Delete a todo"""
  global todos
  todos = [todo for todo in todos if todo["id"] != todo_id]
  if len(todos) < len(todos) + 1:
    return { "message": "Todo deleted successfully" }
  return { "message": "No todo found for the corresponding ID to delete" }

#Delete todo
# @app.delete("/todos/{todo_id}")
# async def delete_todo(todo_id: int):
#   """Delete a todo"""
#   for todo in todos:
#     if todo["id"] == todo_id:
#       todos.remove(todo)
#       return { "message": "Todo deleted successfully" }
#   return { "message": "No todo found for the corresponding ID to delete" }
