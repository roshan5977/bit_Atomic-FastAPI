from sqlalchemy.orm import Session
from model.user import User
from schemas.user_schemas import UserCreate


# geting user by userid
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# geting user by usermail


def get_user_byemail(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


# save user
def save_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(email=user.email, username=user.username, password=user.password, is_active=user.is_active,
                   role=user.role, created_by=user.created_by, updated_by=user.updated_by)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# update user by userid


# def update_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()

# delete user by userid


# def delete_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()


# geting all user by skip and limit

def get_all_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


# deactivate user by userid
def deactivate_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    user.is_active = False
    db.commit()
    db.refresh(user)
    return user
