from sqlalchemy.orm import Session
from model.pomodoro_task import PomodoroTask
from schemas.pomodoro_task_schemas import PomodoroSchema, PomodoroTaskCreate

# geting user by userid


def get_tasks(db: Session, user_id: int):
    return db.query(PomodoroTask).filter(PomodoroTask.user_id == user_id and PomodoroTask.is_completed == False).all()


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


# # delete user by userid

# # def delete_user(db: Session, user_id: int):
# #     return db.query(User).filter(User.id == user_id).first()


# # patch tasks to completeas true
