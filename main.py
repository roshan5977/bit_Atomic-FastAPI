from fastapi import FastAPI
from sqlalchemy.orm import Session
import model
import schemas.pomodoro_task_schemas as pomodoro_task_schemas
import schemas.user_schemas as user_schemas
import schemas.habit_schemas as habit_schemas
import crud.pomodoro_task_crud as pomodoro_task_cruds
import crud.user_crud as user_cruds
import crud.habit_crud as habit_cruds
from fastapi import Depends, FastAPI
from database import SessionLocal, engine


# creating tables in database
model.user.Base.metadata.create_all(bind=engine)
model.pomodoro_task.Base.metadata.create_all(bind=engine)
model.habit.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Test
@app.get("/")
def test():
    return {"status": "success"}


# ______________________________user api________________________________________________


# register user
@app.post("/user/saveusers/", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    print(user.email, '================================')
    # db_user = user_cruds.get_user(db, email=user)
    # print(db_user, '================================')
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return user_cruds.save_user(db=db, user=user)

# get all users


@app.get("/users/", response_model=list[user_schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_cruds.get_all_users(db, skip=skip, limit=limit)
    return users


# get user by userid
# @app.get("/user/{user_id}", response_model=UserSchema.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = user_crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# login user

# deactive user

# _____________________________________habit api _____________________________________________________


# ->  save habit
@app.post("/habit/savehabit/", response_model=habit_schemas.Habit)
def create_habit(habit: habit_schemas.HabitCreate, db: Session = Depends(get_db)):
    return habit_cruds.save_habit(db=db, habit=habit)


# ->  getall habits
@app.get("/habit/getallhabits", response_model=list[habit_schemas.Habit])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    habits = habit_cruds.get_all_habits(skip=skip, limit=limit, db=db)
    return habits

# -> update habit


@app.post("/habit/updatehabit/", response_model=habit_schemas.Habit)
def update_habit(habit: habit_schemas.HabitCreate, db: Session = Depends(get_db)):
    return habit_cruds.update_habit(db=db, habit=habit)

# -> save habit analytics


@app.post("/habitanalytics/savehabitanalytics/", response_model=habit_schemas.HabitAnalysisCreate)
def create_habit(habit_analystics_create: habit_schemas.HabitAnalysisCreate, db: Session = Depends(get_db)):
    return habit_cruds.save_habitanalytics(db=db, HabitAnalysiscreating=habit_analystics_create)

#  ->get all habit analytics for habitid


@app.get("/habitanalytics/getallhabits/{habit_id}", response_model=list[habit_schemas.HabitAnalytics])
def read_users(habit_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    habits = habit_cruds.get_all_habits_analytics(
        db=db, skip=skip, limit=limit, habit_id=habit_id)
    return habits


# ->  save pomodoro task


@app.post("/pomodoro/savetask/", response_model=pomodoro_task_schemas.PomodoroTask)
def create_habit(pomodoro: pomodoro_task_schemas.PomodoroTaskCreate, db: Session = Depends(get_db)):
    return pomodoro_task_cruds.save_task(db=db, pomodoro=pomodoro)


# get pomodoro_task by id
@app.get("/pomodoro/gettask/{user_id}", response_model=list[pomodoro_task_schemas.PomodoroTask])
def read_task(user_id: int, db: Session = Depends(get_db)):
    db_task = pomodoro_task_cruds.get_tasks(db, user_id=user_id)
    return db_task

# change pomodoro_task to completed task


@app.patch("/pomodoro/iscompleted/{p_id}", response_model=pomodoro_task_schemas.PomodoroTask)
def change_is_tasks_complete(p_id: int, db: Session = Depends(get_db)):
    db_task = pomodoro_task_cruds.change_is_tasks_complete(db, p_id=p_id)
    return db_task

# delete pomodorotasks


@app.delete("/pomodoro/deletetasks/{p_id}", response_model=str)
def delete_tasks(p_id: int, db: Session = Depends(get_db)):
    db_task = pomodoro_task_cruds.delete_tasks(db, p_id=p_id)
    return db_task


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
