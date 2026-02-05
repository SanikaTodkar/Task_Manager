from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# Request Schemas
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

# Response Schemas
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool
    created_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)