from sqlalchemy.orm import selectinload
from sqlalchemy.orm import Session
from model.habit import Habit, HabitAnalysis
from schemas.habit_schemas import HabitCreate, HabitAnalysisCreate


# save habit
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

# get all habits


def get_all_habits(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Habit).offset(skip).limit(limit).options(selectinload(Habit.habit_analysis)).all()

# update habit
def update_habit(db: Session, habit: HabitCreate):
    db_habit = db.query(Habit).filter(
        Habit.habit_id == habit.habit_id).first()
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    if db_habit is None:
        raise Exception(status_code=404, detail="Habit not found")
    return db_habit


# save habit analysis
def save_habitanalytics(db: Session, HabitAnalysiscreating: HabitAnalysisCreate):
    db_habit = db.query(Habit).filter(
        Habit.habit_id == HabitAnalysiscreating.habit_id).first()
    if db_habit is None:
        raise Exception(status_code=404, detail="Habit not found")
    habit_analytics_everyday = HabitAnalysis(
        habit_date=HabitAnalysiscreating.habit_date,
        is_performed=HabitAnalysiscreating.is_performed,
        habit_id=HabitAnalysiscreating.habit_id
    )
    db.add(habit_analytics_everyday)
    db.commit()
    db.refresh(habit_analytics_everyday)
    return habit_analytics_everyday

# get all habit analytics by habitid
def get_all_habits_analytics(db: Session, skip: int = 0, limit: int = 10, habitid: int = 1):
    return db.query(HabitAnalysis).filter(
        HabitAnalysis.habit_id == habitid).offset(skip).limit(limit).all()
