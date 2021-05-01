import json

from config.db import conn
from config.credentials import binance_key, binance_secret
from modules.counter import analyze_thread
from modules.repositories import get_all_threads, store_rating
from binance.client import Client
from modules.coinlist import get_binance_coins_with_keywords

binance_client = Client(api_key=binance_key, api_secret=binance_secret)
binance_coins = get_binance_coins_with_keywords(binance_client)

threads = get_all_threads(conn)
for r in threads:
    r['replies'] = json.loads(r.get('replies'))
    result = analyze_thread(r, binance_coins)
    store_rating(conn, result, len(r['replies']), r.get('thread_id'))
