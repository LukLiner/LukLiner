from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, UniqueConstraint

from .base import Base

class User(Base):
    username:Mapped[str] = mapped_column(String(100), unique=True)
    foo: Mapped[int]
    bar: Mapped[int]

    __table_args__ = (UniqueConstraint('foo','bar'),
                      )