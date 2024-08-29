# Python
import os
from typing import Union, Dict, List

import requests
from dotenv import load_dotenv

load_dotenv()
server_url = os.getenv("SERVER_URL")
server_url_v2 = os.getenv("SERVER_URL_V2")


# server_url = os.getenv("LOCAL_URL")
# server_url_v2 = os.getenv("LOCAL_URL_V2")


def login_request(data: dict) -> bool:
    login_url = f"{server_url}/login"

    with requests.Session() as session:
        try:
            r = session.post(url=login_url, json={**data})
            r.raise_for_status()

            # print(r.json())
            if r.status_code == 200:
                return True
            else:
                return False
        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching login: {e}")
            return False


def monitoring_tyype_request(data: dict) -> bool:
    monitoring_url = f"{server_url}/monitoring"
    with requests.Session() as session:
        try:
            r = requests.post(url=monitoring_url, json={**data})

            if r.status_code == 200:
                return True
            else:
                return False
        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching choose type monitoring: {e}")
            return False


def user_detail_request(user_id: int) -> Union[Dict, List]:
    user_detail_url = f"{server_url}/list/?search={user_id}"

    with requests.Session() as session:
        try:
            response = session.get(url=user_detail_url)
            response.raise_for_status()

            data = response.json()
            return data[0] if data else []

        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching user details: {e}")
            return []


def notify_on_off_request(user_id: int, is_send: bool) -> bool:
    notify_url = f"{server_url}/list/change-user-status/?user_id={user_id}&is_send={is_send}"

    with requests.Session() as session:
        try:
            r = session.get(url=notify_url)
            r.raise_for_status()

            if r.status_code == 200:
                return True
            else:
                return False
        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching change notify status: {e}")
            return False


def ip_address_request(user_id: int) -> Union[List, bool]:
    ip_address_url = f"{server_url_v2}/company/devices-address/?user_id={user_id}"

    with requests.Session() as session:
        try:
            r = session.get(url=ip_address_url)
            r.raise_for_status()

            if r.status_code == 200:
                response = r.json()
                data = response.json().get('message', '')
                return data if data else False
            else:
                return False
        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching change notify status: {e}")
            return False
