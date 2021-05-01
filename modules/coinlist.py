from binance.client import Client


def get_binance_coins_with_keywords(client: Client):
    info = client.get_all_coins_info()

    """
    JST is 'just coin' - stopword coin :-)
    """
    variation_blacklist=['JST', 'FOR', 'ONE']
    coin_keywords = {}
    for item in info:
        name = str(item.get('name'))
        symbol = item.get('coin')
        if symbol in variation_blacklist:
            variations = [
                symbol,

                symbol[0].upper() + symbol[1:].lower(),
                name.upper(),
            ]
        else:
            variations = [
                symbol,
                symbol.lower(),
                symbol[0].upper() + symbol[1:].lower(),
                name.lower(),
                name.upper(),
                name[0].upper() + name[1:].lower()

            ]

        coin_keywords[symbol] = set(variations)

    return coin_keywords
