# Python
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

# Project
from app.messages import MainMessages
from app.utilits.request import user_detail_request

main_message = MainMessages()

router = Router()


@router.message(Command("me"))
async def user_info(message: Message):
    get_user_info = await user_detail_request(user_id=message.from_user.id)
    if isinstance(get_user_info, dict):
        company_info = get_user_info.get('company')
        company_name = company_info.get('name', None) if isinstance(company_info, dict) else None

        device_info = get_user_info.get('device')
        device_mac_address = device_info.get('mac_address', None) if isinstance(device_info, dict) else None

        last_updated = get_user_info.get('last_updated', None)
        if last_updated:
            last_updated = last_updated.split('T')[0]

        await message.answer(
            main_message.user_me_message(username=message.from_user.username,
                                         is_send=get_user_info.get('is_send', None),
                                         created_date=get_user_info.get('created_date', None),
                                         last_updated=get_user_info.get('last_updated', None).split('T')[0],
                                         company=company_name,
                                         device=device_mac_address))
    if isinstance(get_user_info, list):
        await message.answer(main_message.user_not_found())
