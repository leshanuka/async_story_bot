from app.database.requests import get_all_types, get_all_stories, get_all_acts, get_all_plots
from sqlalchemy import select, funcfilter

from app.database.models import async_session


async def get_chosen():
    async with async_session() as sessiion:
        result = await sessiion.query(Stories).filter(Stories.sto_type == 'sto')
        print(result)
        return result


    kb = [
        [types.KeyboardButton(text="С пюрешкой")],
        [types.KeyboardButton(text="Без пюрешки")]
    ]


    kb = [
        [
            types.KeyboardButton(text="С пюрешкой"),
            types.KeyboardButton(text="Без пюрешки")
        ],
    ]
