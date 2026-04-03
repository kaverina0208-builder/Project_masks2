import requests
import os
from dotenv import load_dotenv

load_dotenv()

APY_KEY = os.getenv('APY_KEY')

def conversion_amount(transaction_data: dict) -> float:
    url = "https://api.apilayer.com/exchangerates_data/convert"

    headers = {
    'apikey': f'{APY_KEY}'
}

    response = requests.get(url, headers=headers, params=transaction_data)

    if response.status_code != 200:
        raise ValueError(f"Не удалось получить курс валюты")
    result = response.json()['result']
    return result


payload = {
    "amount": "1200",
    "from": "EUR",
    "to": "RUB"
}
if __name__ == '__main__':
    print(conversion_amount(payload))