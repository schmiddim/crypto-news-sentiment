import re


def count_total(symbols: dict, symbol_dict: dict):
    """
    Count Symbols in another dict
    :param symbols:
    :param symbol_dict:
    :return:
    """

    for symbol in symbols:
        if symbol_dict.get(symbol, None) is None:
            symbol_dict[symbol] = 1
        else:
            symbol_dict[symbol] += 1
    return symbol_dict


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
