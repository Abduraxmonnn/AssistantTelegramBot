# Python
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

# Project
from app.messages import MainMessages, ButtonMessages
from app.states import MonitoringTypeState
from app.buttons import reply as btn
from app.utilits import monitoring_type_request
from app.utilits.message_valid import is_valid_monitoring_type
from images.image_ids import end_process_image_id

main_message = MainMessages()
btn_message = ButtonMessages()

router = Router()


@router.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f"ID: {message.photo[-1].file_id}")


@router.message(F.text.lower().contains(btn_message.back_to_monitoring_type_message().lower()))
async def monitoring_type(message: Message):
    await message.answer(main_message.help_message(), reply_markup=btn.type_monitoring)


@router.message(is_valid_monitoring_type)
async def login(message: Message, state: FSMContext):
    msg = message.text.lower()

    if msg == btn_message.type_monitoring_device_message().lower():
        await state.set_state(MonitoringTypeState.device_serial_number)
        await message.answer(main_message.ask_device_serial_message())
    elif msg == btn_message.type_monitoring_company_message().lower():
        await state.set_state(MonitoringTypeState.inn)
        await message.answer(main_message.ask_company_inn_message())
    else:
        await message.answer(main_message.error_choose_one_message())


@router.message(MonitoringTypeState.device_serial_number)
async def check_device_serial_number(message: Message, state: FSMContext):
    await state.update_data(device_serial_number=message.text)

    data = await state.get_data()
    data.update({'user_id': message.from_user.id})
    response = await monitoring_type_request(data=data)
    await state.clear()

    if response:
        await message.answer_photo(photo=end_process_image_id)
        await message.answer(main_message.success_end_process_message())
    else:
        await message.answer(main_message.fail_end_process_message(), reply_markup=btn.type_monitoring)


@router.message(F.text.lower().contains(main_message.ask_company_inn_message().lower()))
@router.message(MonitoringTypeState.inn)
async def check_inn(message: Message, state: FSMContext):
    await state.update_data(inn=message.text)

    data = await state.get_data()
    data.update({'user_id': message.from_user.id})
    response = await monitoring_type_request(data=data)
    await state.clear()

    if response:
        await message.answer_photo(photo=end_process_image_id)
        await message.answer(main_message.success_end_process_message())
    else:
        await message.answer(main_message.fail_end_process_message(), reply_markup=btn.type_monitoring)

# @router.message()
# async def get_photo_id(message: Message):
#     print(message.from_user)
