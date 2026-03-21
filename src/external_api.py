import requests


def conversion_amount(transaction_data: dict) -> float:
    url = "https://api.apilayer.com/exchangerates_data/convert"

    headers = {
        "apikey": "fkPegRUcYuoPK91U6iYpNHi2Gm980pi1"
    }

    response = requests.get(url, headers=headers, params=transaction_data)

    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rate")
    result = response.json()['result']
    if not result:
        raise ValueError(f"No data for currency")

    return result


payload = {
    "amount": "1200",
    "from": "EUR",
    "to": "USD"
}
if __name__ == '__main__':
    print(conversion_amount(payload))