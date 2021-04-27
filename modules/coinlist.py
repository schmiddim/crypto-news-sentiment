from binance.client import Client


def get_binance_coins_with_keywords(client: Client):
    info = client.get_all_coins_info()

    coin_keywords = {}
    for item in info:
        name = str(item.get('name'))

        variations = [
            item.get('coin'),
            item.get('coin').lower(),
            name.lower(),
            name.upper(),
            name[0].upper() + name[1:].lower()

        ]

        coin_keywords[item.get('coin')]= set(variations)

    return coin_keywords