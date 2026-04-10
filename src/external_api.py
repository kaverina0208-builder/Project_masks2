import requests
import os
from dotenv import load_dotenv

load_dotenv()

APY_KEY = os.getenv("APY_KEY")


def conversion_amount(transaction_data: dict) -> float:
    """The function converts the amount to the desired currency"""

    if transaction_data['operationAmount']['currency']['code'] == 'RUB':
        result = transaction_data['operationAmount']['amount']

    else:
        url = "https://api.apilayer.com/exchangerates_data/convert"

        headers = {"apikey": f"{APY_KEY}"}

        payload = {
            "amount": transaction_data['operationAmount']['amount'],
            "from": transaction_data['operationAmount']['currency']['code'],
            "to": "RUB"
        }

        response = requests.get(url, headers=headers, params=payload)

        if response.status_code != 200:
            raise ValueError("Не удалось получить курс валюты")
        result = response.json()["result"]
    return result


tran_data = {
  "id": 41428829,
  "state": "EXECUTED",
  "date": "2019-07-03T18:35:29.512364",
  "operationAmount": {
    "amount": "100",
    "currency": {
      "name": "USD",
      "code": "USD"
    }
  },
  "description": "Перевод организации",
  "from": "MasterCard 7158300734726758",
  "to": "Счет 35383033474447895560"
}

if __name__ == "__main__":
    print(conversion_amount(tran_data))
