from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from model.base_model import Base, intpk, str100

class User(Base):
    __tablename__ = "user"

    id: Mapped[intpk]
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    first_name: Mapped[str100 | None] = mapped_column(String(100))
    last_name: Mapped[str100 | None] = mapped_column(String(100))
