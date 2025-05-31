import requests
from config import SMM_API_KEY, SMM_API_URL

def create_order(service_id, link, quantity):
    payload = {
        "key": SMM_API_KEY,
        "action": "add",
        "service": service_id,
        "link": link,
        "quantity": quantity
    }
    response = requests.post(SMM_API_URL, data=payload)
    return response.json()
