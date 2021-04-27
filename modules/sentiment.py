from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np


class Sentiment:

    def categorize_headlines(self, headlines, keywords):

        categorized_headlines = {}
        # this loop will create a dictionary for each keyword defined
        for keyword in keywords:
            categorized_headlines['{0}'.format(keyword)] = []
        # keyword needs to be a loop in order to be able to append headline to the correct dictionary
        for keyword in keywords:
            # @todo match only standalones!
            # FOR matches on
            #
            # ['Polygon co-founder raises $2.2M for India COVID-19 relief ',
            #  'Binance crypto exchange to launch its own NFT platform',
            #  'Iran’s central bank says officially mined crypto can be used to pay for imports',
            #  'Irish crypto firms must comply with money laundering laws for the first time']
            # looping through each headline is required as well
            for headline in headlines['title']:
                # appends the headline containing the keyword to the correct dictionary
                if any(key in headline for key in keywords[keyword]):
                    categorized_headlines[keyword].append(headline)
        return categorized_headlines

    def analyse_headlines(self, categorised_headlines):
        '''Analyse categorised headlines and return NLP scores'''
        sia = SentimentIntensityAnalyzer()

        sentiment = {}

        for coin in categorised_headlines:
            if len(categorised_headlines[coin]) > 0:
                # create dict for each coin
                sentiment['{0}'.format(coin)] = []
                # append sentiment to dict
                for title in categorised_headlines[coin]:
                    sentiment[coin].append(sia.polarity_scores(title))

        return sentiment

    def compile_sentiment(self, sentiment):
        '''Arranges every compound value into a list for each coin'''

        compiled_sentiment = {}

        for coin in sentiment:
            compiled_sentiment[coin] = []

            for item in sentiment[coin]:
                # append each compound value to each coin's dict
                compiled_sentiment[coin].append(sentiment[coin][sentiment[coin].index(item)]['compound'])

        return compiled_sentiment

    def compound_average(self, compiled_sentiment):
        '''Calculates and returns the average compoud sentiment for each coin'''

        headlines_analysed = {}

        for coin in compiled_sentiment:
            headlines_analysed[coin] = len(compiled_sentiment[coin])

            # calculate the average using numpy if there is more than 1 element in list
            compiled_sentiment[coin] = np.array(compiled_sentiment[coin])

            # get the mean
            compiled_sentiment[coin] = np.mean(compiled_sentiment[coin])

            # convert to scalar
            compiled_sentiment[coin] = compiled_sentiment[coin].item()

        return compiled_sentiment, headlines_analysed

    def get_signals(self, compiled_sentiment, headlines_analysed):
        SENTIMENT_THRESHOLD = 0
        NEGATIVE_SENTIMENT_THRESHOLD = 0

        # define the minimum number of articles that need to be analysed in order
        # for the sentiment analysis to qualify for a trade signal
        # avoid using 1 as that's not representative of the overall sentiment
        MINUMUM_ARTICLES = 1

        for coin in compiled_sentiment:

            # check if the sentiment and number of articles are over the given threshold
            if compiled_sentiment[coin] > SENTIMENT_THRESHOLD and headlines_analysed[coin] >= MINUMUM_ARTICLES:
                print('buy {}, compiled {}'.format(coin,compiled_sentiment[coin]))
            else:
                print('do not buy {}, compiled {}'.format(coin,compiled_sentiment[coin]))

            if compiled_sentiment[coin] < NEGATIVE_SENTIMENT_THRESHOLD and headlines_analysed[coin] >= MINUMUM_ARTICLES:
                print('SELL {}, compiled {}'.format(coin, compiled_sentiment[coin]))
            else:
                print('do not SELL {}, compiled {}'.format(coin, compiled_sentiment[coin]))

