import asyncio
from sqlalchemy import String, create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from config import settings
from typing import Optional, Annotated



sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    #pool_size=5,
    #max_overflow=10
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
    #pool_size=5,
    #max_overflow=10
)






#with engine.connect() as conn:
#    res = conn.execute(text("SELECT VERSION()"))
#    print(f"{res.first()=}")


#async def get123():
#    async with async_engine.connect() as conn:
#        res = await conn.execute(text("SELECT VERSION()"))
#        print(f"{res.first()=}")
#
#
#asyncio.run(get123())

session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }
