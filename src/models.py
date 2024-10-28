from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, text
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional, Annotated
import enum
import datetime








class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]



class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"



class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    compensation: Mapped[Optional[int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelte="CASCADE"))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                           onupdate= datetime.datetime.utcnow)









metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)#imperative стиль обявление табл 




