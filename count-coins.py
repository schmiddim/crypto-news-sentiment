from config.db import conn
import json
from binance.client import Client
from config.credentials import binance_key, binance_secret

from modules.coinlist import get_binance_coins_with_keywords
from modules.counter import count_unique_symbols_in_string, count_total

sql = """SELECT * FROM threads WHERE thread_id=%s"""

cur = conn.cursor()
cur.execute(sql, [34221041])
r = cur.fetchone()
r['replies'] = json.loads(r.get('replies'))

binance_client = Client(api_key=binance_key, api_secret=binance_secret)
binance_coins = get_binance_coins_with_keywords(binance_client)


le_dict = {}

for comment in r['replies'] :
    string = comment.get('comment')

    r = count_unique_symbols_in_string(string, binance_coins)
    le_dict = count_total(r, le_dict)
print(sorted(le_dict.items(), key=lambda x: x[1],reverse=True))
