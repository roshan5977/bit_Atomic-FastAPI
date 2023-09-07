from sqlalchemy import Boolean, Column, String, Integer, DateTime, Time
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    awake_time = Column(Time)
    sleep_time = Column(Time)
    created_by = Column(String)
    created_on = Column(DateTime)
    updated_by = Column(String)
    updated_on = Column(DateTime)
    last_login = Column(DateTime)
    role = Column(String)
    is_active = Column(Boolean)


