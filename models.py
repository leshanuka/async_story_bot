from sqlalchemy import BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import  SQLALCHEMY_URL

engine = create_async_engine(SQLALCHEMY_URL, echo = True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class Stories(Base):
    __tablename__ = 'stories'

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column()
    stat_type: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    stat_stories: Mapped[str] = mapped_column()
    next_level: Mapped[int] = mapped_column()


class Types(Base):
    __tablename__ = 'types'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    stat: Mapped[str] = mapped_column()
    next_level: Mapped[int] = mapped_column()


class Acts(Base):
    __tablename__ = 'acts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    stat_types: Mapped[str] = mapped_column()
    stat_stories: Mapped[str] = mapped_column()
    stat: Mapped[str] = mapped_column()
    next_level: Mapped[int] = mapped_column()


class Plots(Base):
    __tablename__ = 'plot'

    id: Mapped[int] = mapped_column(primary_key=True)
    story: Mapped[str] = mapped_column()
    act: Mapped[str] = mapped_column()
    stat: Mapped[str] = mapped_column()
    text: Mapped[str] = mapped_column()
    if_attach: Mapped[str] = mapped_column()
    path_attach: Mapped[str] = mapped_column()
    health: Mapped[str] = mapped_column()
    num: Mapped[int] = mapped_column()
    opt_1: Mapped[str] = mapped_column()
    stat_1: Mapped[str] = mapped_column()
    opt_2: Mapped[str] = mapped_column()
    stat_2: Mapped[str] = mapped_column()
    opt_3: Mapped[str] = mapped_column()
    stat_3: Mapped[str] = mapped_column()
    opt_4: Mapped[str] = mapped_column()
    stat_4: Mapped[str] = mapped_column()
    opt_5: Mapped[str] = mapped_column()
    stat_5: Mapped[str] = mapped_column()
    opt_6: Mapped[str] = mapped_column()
    stat_6: Mapped[str] = mapped_column()
    opt_7: Mapped[str] = mapped_column()
    stat_7: Mapped[str] = mapped_column()
    opt_8: Mapped[str] = mapped_column()
    stat_8: Mapped[str] = mapped_column()
    opt_9: Mapped[str] = mapped_column()
    stat_9: Mapped[str] = mapped_column()
    opt_10: Mapped[str] = mapped_column()
    stat_10: Mapped[str] = mapped_column()
    opt_11: Mapped[str] = mapped_column()
    stat_11: Mapped[str] = mapped_column()
    opt_12: Mapped[str] = mapped_column()
    stat_12: Mapped[str] = mapped_column()



class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column()
    stat_types: Mapped[str] = mapped_column()
    stat_stories: Mapped[str] = mapped_column()
    stat: Mapped[str] = mapped_column()
    next_level: Mapped[int] = mapped_column()




async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)




