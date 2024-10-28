from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]


























metadata_obj = MetaData()



workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)#imperative стиль обявление табл 
