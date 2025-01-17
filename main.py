"""main file for the app"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  """basic hello world"""
  return {"message": "Hello World"}

todos = [

]

# Get all todos

# Get a single todo

# Creata todo

# Update todo

# Delete todo