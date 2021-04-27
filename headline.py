import asyncio
from binance.client import Client
from config.credentials import binance_key, binance_secret
from modules.coinlist import get_binance_coins_with_keywords
from modules.news import FromCsvFeeds
from modules.sentiment import Sentiment

from_csv = FromCsvFeeds('Crypto feeds.csv')
binance_client = Client(api_key=binance_key, api_secret=binance_secret)


async def main():
    headlines = await from_csv.get_by_csv(24)
    binance_coins = get_binance_coins_with_keywords(binance_client)




    sen = Sentiment()
    categorized_headlines = sen.categorize_headlines(headlines, binance_coins)
    sentiment = sen.analyse_headlines(categorized_headlines)
    compiled_sentiment = sen.compile_sentiment(sentiment)
    compiled_sentiment, headlines_analysed = sen.compound_average(compiled_sentiment)
    sen.get_signals(compiled_sentiment,headlines_analysed)

asyncio.run(main())
