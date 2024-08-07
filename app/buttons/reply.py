# Python
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Project
from app.messages.button_message import ButtonMessages

custom_message = ButtonMessages()

type_monitoring = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=custom_message.type_monitoring_device_message()),
        KeyboardButton(text=custom_message.type_monitoring_company_message())
    ]
], resize_keyboard=True, one_time_keyboard=True,
    input_field_placeholder=custom_message.type_monitoring_placeholder_message())

get_contacts = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=custom_message.send_contact_message(), request_contact=True),
    ]
], resize_keyboard=True, one_time_keyboard=True)

login = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=custom_message.login_message())
    ]
], resize_keyboard=True, one_time_keyboard=True)
