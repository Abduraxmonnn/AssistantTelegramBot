# Python
import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

# Project
from app.handlers import message_handler, start_handler, login_handler

load_dotenv()

TOKEN = os.getenv("TOKEN")


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        start_handler.router,
        login_handler.router,
        message_handler.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
