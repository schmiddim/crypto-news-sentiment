from binance.client import Client


def get_binance_coins_with_keywords(client: Client):
    info = client.get_all_coins_info()

    coin_keywords = []
    for item in info:
        name = str(item.get('name'))

        variations = [
            item.get('coin'),
            item.get('coin').lower(),
            name.lower(),
            name.upper(),
            name[0].upper() + name[1:].lower()

        ]
        enriched = {
            'coin': item.get('coin'),
            'variations': set(variations)
        }

        coin_keywords.append(enriched)

    return coin_keywords