# Python
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# Project
from app.buttons import reply as btn
from app.messages import MainMessages
from images.image_ids import image_hello_banner_id

main_message = MainMessages()

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer_photo(photo=image_hello_banner_id,
                               caption=main_message.hello_message(message.from_user.username),
                               reply_markup=btn.login)
    # await message.answer(main_message.hello_message(message.from_user.username), reply_markup=btn.login)
