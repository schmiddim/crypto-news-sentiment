import re


def count_total(symbols, symbol_dict: dict):
    """
    Count Symbols in another dict
    :param symbols:
    :param symbol_dict:
    :return
    """

    for symbol in symbols:
        if symbol_dict.get(symbol, None) is None:
            symbol_dict[symbol] = 1
        else:
            symbol_dict[symbol] += 1
    return dict(sorted(symbol_dict.items(), key=lambda item: item[1], reverse=True))


def count_unique_symbols_in_string(string: str, symobl_dict: dict):
    """
    Just counts coins in a string

    :param string:
    :param symobl_dict:
    :return:
    """
    matches = []
    string = re.sub(r'[^\w\s]', '', string)
    for symbol in symobl_dict:
        for coin in symobl_dict.get(symbol):

            if ' ' + coin + ' ' in ' ' + string + ' ':
                matches.append(symbol)

    return set(matches)


def analyze_thread(thread: dict, binance_coins):
    stats = {}
    for comment in thread['replies']:
        string = comment.get('comment')

        result = count_unique_symbols_in_string(string, binance_coins)
        stats = count_total(result, stats)
    return stats
