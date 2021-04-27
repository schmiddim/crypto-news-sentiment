import asyncio
from binance.client import Client
from config.credentials import binance_key, binance_secret
from modules.coinlist import get_binance_coins_with_keywords
from modules.news import FromCsvFeeds

from_csv = FromCsvFeeds('Crypto feeds.csv')
binance_client = Client(api_key=binance_key, api_secret=binance_secret)


async def main():
    headlines = await from_csv.get_by_csv(24)
    binance_coins = get_binance_coins_with_keywords(binance_client)

    #@todo sentiment


asyncio.run(main())
