from sqlalchemy import Boolean, Column, String, Integer, DateTime, Time, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Habit(Base):
    __tablename__ = 'habits'

    habit_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer)
    habit_name = Column(String)
    habit_priority = Column(Integer)
    is_daily_or_weekly = Column(Boolean)
    habit_start_date_time = Column(DateTime)
    is_enable_remainder = Column(Boolean)
    notes_for_quotes = Column(String)
    type_of_habit = Column(String)
    duration = Column(Time)
    # notification_tune
    snoose_duration = Column(Integer)
    best_streak = Column(Integer)
    current_streak = Column(Integer)
    habit_score = Column(Integer)

    habit_analysis = relationship("HabitAnalysis", back_populates="habit")


class HabitAnalysis(Base):
    __tablename__ = 'habit_analysis'

    habit_analysis_id = Column(Integer, autoincrement=True, primary_key=True)
    habit_date = Column(DateTime)
    is_performed = Column(Boolean)
    habit_id = Column(Integer, ForeignKey("habits.habit_id"))

    habit = relationship("Habit", back_populates="habit_analysis")
