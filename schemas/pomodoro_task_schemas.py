from pydantic import BaseModel
from datetime import datetime


class PomodoroTaskBase(BaseModel):
    user_id: int
    task_name: str
    task_date_time_scheduled: datetime
    is_completed: bool


class PomodoroTaskCreate(PomodoroTaskBase):
    pass


class PomodoroTask(PomodoroTaskBase):
    p_id: int

    class Config:
        orm_mode = True
