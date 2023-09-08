from sqlalchemy.orm import Session
from model.pomodoro_task import PomodoroTask
from schemas.pomodoro_task_schemas import PomodoroTaskCreate

# geting user by userid
def get_tasks(db: Session, user_id: int):
    return db.query(PomodoroTask).filter(PomodoroTask.user_id == user_id).all()


# save pomodorotask
def save_task(db: Session, pomodoro: PomodoroTaskCreate):
    db_pomo_task = PomodoroTask(user_id=pomodoro.user_id,
                                task_name=pomodoro.task_name,
                                task_date_time_scheduled=pomodoro.task_date_time_scheduled,
                                is_completed=pomodoro.is_completed)
    db.add(db_pomo_task)
    db.commit()
    db.refresh(db_pomo_task)
    return db_pomo_task


# delete user by userid
def delete_tasks(db: Session, p_id: int):
    db.query(PomodoroTask).filter(PomodoroTask.p_id == p_id).delete()
    db.commit()
    return "deleted"+p_id


# patch tasks to completeas true
def change_is_tasks_complete(db: Session, p_id: int):
    pomodoroTask = db.query(PomodoroTask).filter(
        PomodoroTask.p_id == p_id).first()
    if not pomodoroTask:
        return None
    pomodoroTask.is_completed = True
    db.commit()
    db.refresh(pomodoroTask)
    return pomodoroTask
