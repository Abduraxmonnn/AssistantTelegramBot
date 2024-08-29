# Python
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

# Project
from app.messages import MainMessages
from app.utilits.request import notify_on_off_request

main_message = MainMessages()

router = Router()


@router.message(Command("help"))
async def help_command(message: Message):
    # change_notify = notify_on_off_request(user_id=message)
    await message.answer(main_message.help_message())

