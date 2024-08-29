# Python
import asyncio
import os

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

# Project
from app.handlers import message_handler, start_handler, login_handler, notify_on_off_handler, user_info_handler, \
    help_handler, ip_address_handler

load_dotenv()

TOKEN = os.getenv("TOKEN")


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        start_handler.router,
        login_handler.router,
        message_handler.router,
        help_handler.router,
        notify_on_off_handler.router,
        user_info_handler.router,
        ip_address_handler.router
    )

    bot_commands = [
        types.BotCommand(command="/start", description="Start bot for subscribe"),
        types.BotCommand(command="/help", description="Get info about bot"),
        types.BotCommand(command="/notify", description="Notification ON/OFF"),
        types.BotCommand(command="/me", description="Information about User"),
        types.BotCommand(command="/ip_address", description="Get IP address of all company devices"),
    ]

    await bot.set_my_commands(bot_commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
