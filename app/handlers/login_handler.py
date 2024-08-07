# Python
import asyncio

# Aiogram
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

# Project
from app.states import UserState
from app.buttons.reply import get_contacts
from app.messages import MainMessages, ButtonMessages
from app.buttons import reply as btn
from app.utilits import delete_message_delay

main_message = MainMessages()
btn_message = ButtonMessages()

router = Router()


@router.message(F.text.lower() == btn_message.login_message().lower())
async def set_login_username(message: Message, state: FSMContext):
    await state.set_state(UserState.username)
    await message.answer(main_message.login_username_message())


@router.message(UserState.username)
async def get_login_username(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(UserState.password)
    await message.answer(main_message.login_password_message())


@router.message(UserState.password)
async def get_login_username(message: Message, state: FSMContext):
    await state.update_data(password=message.text)

    asyncio.create_task(delete_message_delay(message, 3))

    await state.set_state(UserState.phone_number)
    await message.answer(main_message.login_phone_message(), reply_markup=get_contacts)


@router.message(UserState.phone_number)
async def get_login_username(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)

    data = await state.get_data()
    await state.clear()

    if data['username'] == 'admin' and data['password'] == 'test':
        await message.answer(main_message.login_success_message(), reply_markup=btn.type_monitoring)
    else:
        await message.answer(main_message.login_fail_message(), reply_markup=btn.login)
