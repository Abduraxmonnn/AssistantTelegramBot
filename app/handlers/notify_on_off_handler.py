# Python
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

# Project
from app.messages import MainMessages, ButtonMessages
from app.buttons import reply as btn
from app.utilits.request import notify_on_off_request

main_message = MainMessages()
btn_message = ButtonMessages()

router = Router()


@router.message(Command("notify"))
async def notify_command(message: Message):
    await message.answer(main_message.monitoring_type_message(), reply_markup=btn.notify)


@router.message(F.text.lower().contains(btn_message.notify_status_on_btn_message().lower()))
async def notify_status_on(message: Message):
    notify_info = notify_on_off_request(user_id=message.from_user.id, is_send=True)
    if notify_info:
        await message.answer(main_message.notify_status_on_message(), reply_markup=btn.type_monitoring)
    else:
        await message.answer(main_message.error_on_notify_process_message(), reply_markup=btn.type_monitoring)


@router.message(F.text.lower().contains(btn_message.notify_status_off_btn_message().lower()))
async def notify_status_off(message: Message):
    notify_info = notify_on_off_request(user_id=message.from_user.id, is_send=False)
    if notify_info:
        await message.answer(main_message.notify_status_off_message(), reply_markup=btn.type_monitoring)
    else:
        await message.answer(main_message.error_on_notify_process_message(), reply_markup=btn.type_monitoring)
