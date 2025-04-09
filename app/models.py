from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class ToDoModel(Base):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    status: Mapped[bool]