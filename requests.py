from models import Stories,Types, Acts, Plots, async_session
from sqlalchemy import select


async def get_all_types():
    async with async_session() as sessiion:
        result = await sessiion.scalars(select(Types))
        return result

async def get_all_stories():
    async with async_session() as sessiion:
        result = await sessiion.scalars(select(Stories))
        return result

async def get_all_acts():
    async with async_session() as sessiion:
        result = await sessiion.scalars(select(Acts))
        return result

async def get_all_plots():
    async with async_session() as sessiion:
        result = await sessiion.scalars(select(Plots))
        return result
