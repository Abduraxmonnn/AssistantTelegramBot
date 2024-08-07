# Project
from app.messages import ButtonMessages

btn_message = ButtonMessages()

VALID_MONITORING_TYPES = {
    btn_message.type_monitoring_device_message().lower(),
    btn_message.type_monitoring_company_message().lower(),
}


def is_valid_monitoring_type(message):
    return message.text.lower() in VALID_MONITORING_TYPES
