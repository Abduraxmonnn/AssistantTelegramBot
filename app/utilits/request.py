import os
from typing import Union, Dict, List
import aiohttp
from dotenv import load_dotenv

load_dotenv()
server_url = os.getenv("SERVER_URL")
server_url_v2 = os.getenv("SERVER_URL_V2")
# server_url = os.getenv("LOCAL_URL")
# server_url_v2 = os.getenv("LOCAL_URL_V1")

async def login_request(data: dict) -> bool:
    login_url = f"{server_url}/login/"
    async with aiohttp.ClientSession(trust_env=True) as session:
        try:
            async with session.post(url=login_url, json={**data}, ssl=False) as response:
                response.raise_for_status()
                return response.status == 200
        except (aiohttp.ClientError, ValueError) as e:
            print(f"Error fetching login: {e}")
            return False


async def monitoring_type_request(data: dict) -> bool:
    monitoring_url = f"{server_url}/monitoring/"
    async with aiohttp.ClientSession(trust_env=True) as session:
        converted_serial_number = {
            'device_serial_number': str(data.pop('device_serial_number')).split(' ')
        }
        print('--> converted_serial_number: ', converted_serial_number)
        data.update(converted_serial_number)
        print('--> data: ', data)
        try:
            async with session.post(url=monitoring_url, json={**data}, ssl=False) as response:
                return response.status == 200
        except (aiohttp.ClientError, ValueError) as e:
            print(f"Error fetching choose type monitoring: {e}")
            return False


async def user_detail_request(user_id: int) -> Union[Dict, List]:
    user_detail_url = f"{server_url}/list/?search={user_id}/"
    async with aiohttp.ClientSession(trust_env=True) as session:
        try:
            async with session.get(url=user_detail_url, ssl=False) as response:
                response.raise_for_status()
                data = await response.json()
                return data[0] if data else []
        except (aiohttp.ClientError, ValueError) as e:
            print(f"Error fetching user details: {e}")
            return []


async def notify_on_off_request(user_id: int, is_send: bool) -> bool:
    notify_url = f"{server_url}/list/change-user-status/?user_id={user_id}&is_send={is_send}/"
    async with aiohttp.ClientSession(trust_env=True) as session:
        try:
            async with session.get(url=notify_url, ssl=False) as response:
                response.raise_for_status()
                return response.status == 200
        except (aiohttp.ClientError, ValueError) as e:
            print(f"Error fetching change notify status: {e}")
            return False


async def ip_address_request(user_id: int) -> Union[List, bool]:
    ip_address_url = f"{server_url_v2}/company/devices-address/?user_id={user_id}/"
    async with aiohttp.ClientSession(trust_env=True) as session:
        try:
            async with session.get(url=ip_address_url, ssl=False) as response:
                response.raise_for_status()
                if response.status == 200:
                    response_json = await response.json()
                    data = response_json.get('message', '')
                    return data if data else False
                else:
                    return False
        except (aiohttp.ClientError, ValueError) as e:
            print(f"Error fetching IP address: {e}")
            return False
