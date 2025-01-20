from pydantic import BaseModel

class Todo(BaseModel):
  """
  Represents a Todo item with id, title, and completion status.
  
  Attributes:
      id (int): Unique identifier for the Todo item.
      title (str): Title of the Todo item.
      completed (bool): Completion status of the Todo item.
  """
  id: int
  title: str
  completed: bool