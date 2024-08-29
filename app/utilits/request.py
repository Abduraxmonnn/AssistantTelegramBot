# Python
import os
from typing import Union, Dict, List

import requests
from dotenv import load_dotenv

load_dotenv()
server_url = os.getenv("SERVER_URL")
# server_url = os.getenv("LOCAL_URL")


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
