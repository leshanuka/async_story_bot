import logging
import sys
sys.path.append("/root/async_story_bot")

import asyncio

from aiogram import Bot, Dispatcher

from handlers import router
from models import async_main
from config import TOKEN



async def main():
    await async_main()


    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout, force= True)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
