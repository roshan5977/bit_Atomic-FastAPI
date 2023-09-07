from sqlalchemy import Boolean, Column, String, Integer, DateTime, Time

from database import Base


class PomodoroTask(Base):
    __tablename__ = 'pomodoro_task'

    p_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    task_name = Column(String)
    task_date_time_scheduled = Column(DateTime)
    is_completed = Column(Boolean)
