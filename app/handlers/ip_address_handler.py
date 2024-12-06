# Python
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

# Project
from app.messages import MainMessages
from app.utilits.request import ip_address_request

main_message = MainMessages()

router = Router()


@router.message(Command("ip_address"))
async def ip_address_info(message: Message):
    get_ip_address = await ip_address_request(user_id=message.from_user.id)

    if isinstance(get_ip_address, list):
        data = ""

        for i, item in enumerate(get_ip_address):
            data += f"{item}"
            if i < len(get_ip_address) - 1:
                data += "\n----------\n"
        await message.answer(data)

    if not get_ip_address:
        await message.answer(main_message.error_get_ip_address_message())
