# Python
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Project
from app.messages.button_message import ButtonMessages

button_message = ButtonMessages()

type_monitoring = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=button_message.type_monitoring_device_message()),
        KeyboardButton(text=button_message.type_monitoring_company_message())
    ],
], resize_keyboard=True, one_time_keyboard=True,
    input_field_placeholder=button_message.type_monitoring_placeholder_message())

get_contacts = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=button_message.send_contact_message(), request_contact=True),
    ]
], resize_keyboard=True, one_time_keyboard=True)

login = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=button_message.login_message())
    ]
], resize_keyboard=True, one_time_keyboard=True)

notify = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text=button_message.notify_status_on_btn_message()),
        KeyboardButton(text=button_message.notify_status_off_btn_message())
    ],
    [
        KeyboardButton(text=button_message.back_to_monitoring_type_message()),
    ]
], resize_keyboard=True, one_time_keyboard=True)
