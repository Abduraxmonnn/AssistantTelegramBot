from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    username = State()
    password = State()
    phone_number = State()


class MonitoringTypeState(StatesGroup):
    inn = State()
    device_serial_number = State()
