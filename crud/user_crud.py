from sqlalchemy.orm import Session
from model.user import User
from schemas.user_schemas import UserCreate, UserLogin, Email
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, username: str):
    pass


def authenticate_user(email: str, password: str, db: Session):
    user = get_user_byemail(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user

# async def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)]
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


def reset_password(email: str, password: str, db: Session):
    hashed_password = get_password_hash(password)
    user = get_user_byemail(db, email)
    if not user:
        return Exception()
    user.password = hashed_password
    db.commit()
    db.refresh(user)
    return user

# send otp to email


def send_email(email: str):
    print(email)
    # Your email and password (you may want to use environment variables for security)
    sender_email = "bitatomicadmn@gmail.com"
    sender_password = ""
    # Create a secure connection with the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    print(email)
    # Log in to your email account
    server.login(sender_email, sender_password)

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email.to_email
    message["Subject"] = "check"

    # Attach the email body
    message.attach(
        MIMEText('Hi This is from bitAtomic \n your otp is 8773', "plain"))

    # Send the email
    server.sendmail(sender_email, email.to_email, message.as_string())
    server.quit()

    return "Email sent successfully"
