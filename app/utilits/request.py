# Python
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def login_request(data: dict) -> bool:
    # login_url = os.getenv("LOCAL_URL_LOGIN")
    login_url = os.getenv("SERVER_URL_LOGIN")
    r = requests.post(url=login_url, json={**data})
    
   #  print(r.json())
    if r.status_code == 200:
        return True
    else:
        return False


def monitoring_tyype_request(data: dict) -> bool:
    # monitoring_url = os.getenv("LOCAL_URL_MONITORING")
    monitoring_url = os.getenv("SERVER_URL_MONITORING")
    r = requests.post(url=monitoring_url, json={**data})

    if r.status_code == 200:
        return True
    else:
        return False
