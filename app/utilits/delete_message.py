import asyncio

from aiogram.types import Message


async def delete_message_delay(message: Message, delay: int):
    """
    Delete message after delay seconds

    :param message:
    :param delay:
    :return:
    """
    await asyncio.sleep(delay)
    await message.delete()
