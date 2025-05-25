from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, UniqueConstraint

from .base import Base
from .mixins.int_id_primary_key import IntIdPkMixin


class User(Base, IntIdPkMixin):
    username:Mapped[str] = mapped_column(String(100), unique=True)
    foo: Mapped[int]
    bar: Mapped[int]

    __table_args__ = (UniqueConstraint('foo','bar'),
                      )