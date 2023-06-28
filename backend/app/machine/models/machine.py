from sqlalchemy import Column, String, Integer, Boolean

from core.db import Base
from core.db.mixins import TimestampMixin


class Machine(Base, TimestampMixin):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False, default="Machine")
    location = Column(String(50), nullable=True)
    email = Column(String(50), nullable=False, unique=True)
    number = Column(String(200), nullable=False, unique=True)
    enum = Column(Boolean, nullable=False, default=False)
