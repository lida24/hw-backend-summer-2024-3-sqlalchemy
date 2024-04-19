from dataclasses import dataclass
from hashlib import sha256

from aiohttp_session import Session
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.store.database.sqlalchemy_base import BaseModel


@dataclass
class Admin:
    id: int
    email: str
    password: str | None = None

    @staticmethod
    def hash_password(password: str) -> str:
        return sha256(password.encode()).hexdigest()

    @classmethod
    def get_current_session(cls, session: Session) -> "Admin":
        return cls(id=session["admin"]["id"], email=session["admin"]["email"])


class AdminModel(BaseModel):
    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120), nullable=False)

    def is_password_valid(self, password: str) -> bool:
        return self.password == Admin.hash_password(password)
