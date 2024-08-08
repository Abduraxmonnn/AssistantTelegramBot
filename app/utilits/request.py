# Python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SERVER")


def login_request(data: dict) -> bool:
    r = requests.post(url=url, json={**data})

    if r.status_code == 200:
        return True
    else:
        return False


def monitoring_tyype_request(data: dict) -> bool:
    print(data)
    r = requests.post(url=url, json={**data})

    if r.status_code == 200:
        return True
    else:
        return False
