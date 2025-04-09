from pydantic import BaseModel, Field, ConfigDict


class TasksBaseShemas(BaseModel):
    title: str = Field(..., max_length=128, min_length=10)
    description: str = Field(..., max_length=1000)
    status: bool

    model_config = ConfigDict(from_attributes=True)


class TasksCreateShemas(TasksBaseShemas):
    id: int = Field(..., gt=0)