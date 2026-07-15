from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Recipe(Base):
    __tablename__ = "recipe"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str] = mapped_column(String, nullable=False)

    instructions: Mapped[str] = mapped_column(String, nullable=False)

    imageUrl: Mapped[str] = mapped_column(String, nullable=False)

    cookTime: Mapped[str] = mapped_column(String, nullable=False)

    difficulty: Mapped[str] = mapped_column(String, nullable=False)

    userId: Mapped[str] = mapped_column(String, nullable=False)
