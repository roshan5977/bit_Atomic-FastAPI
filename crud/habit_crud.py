from sqlalchemy.orm import Session
from model.habit import Habit, HabitAnalysis
from schemas.habit_schemas import HabitCreate


# /post
# save user
def save_habit(db: Session, habit: HabitCreate):
    new_habit = Habit(
        user_id=habit.user_id,
        habit_name=habit.habit_name,
        habit_priority=habit.habit_priority,
        is_daily_or_weekly=habit.is_daily_or_weekly,
        is_enable_remainder=habit.is_enable_remainder,
        habit_start_date_time=habit.habit_start_date_time,
        notes_for_quotes=habit.notes_for_quotes,
        type_of_habit=habit.type_of_habit,
        duration=habit.duration,
        snoose_duration=habit.snoose_duration,
        best_streak=habit.best_streak,
        current_streak=habit.current_streak,
        habit_score=habit.habit_score
    )
    db.add(new_habit)
    db.commit()
    db.refresh(new_habit)
    return new_habit


# patch       ispending


# getallhabit
# geting all habits by skip and limit

def get_all_habits(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Habit).offset(skip).limit(limit).all()
