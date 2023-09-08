from pydantic import BaseModel
from datetime import datetime, time
from typing import List


class HabitAnalysisBase(BaseModel):
    habit_date: datetime
    is_performed: bool
    habit_id: int


class HabitAnalysisCreate(HabitAnalysisBase):
    pass


class HabitAnalysis(HabitAnalysisBase):
    habit_analysis_id: int

    class Config:
        orm_mode = True


class HabitBase(BaseModel):
    user_id: int
    habit_name: str
    habit_priority: int
    is_daily_or_weekly: bool
    habit_start_date_time: datetime
    is_enable_remainder: bool
    notes_for_quotes: str
    type_of_habit: str
    duration: time
    snoose_duration: int
    best_streak: int
    current_streak: int
    habit_score: int


class HabitCreate(HabitBase):
    pass


class Habit(HabitBase):
    habit_id: int
    habit_analysis: List[HabitAnalysis]

    class Config:
        orm_mode = True
