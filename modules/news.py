import asyncio
import csv
import logging
import os
import xml.etree.ElementTree as Et
from datetime import datetime

import aiohttp
import pytz


class FromCsvFeeds:
    csv_file = None

    headlines = {'source': [], 'title': [], 'pubDate': []}

    def __init__(self, csv_file):
        if False is os.path.isfile(csv_file):
            raise Exception("file {} not found".format(csv_file))
        self.csv_file = csv_file

    async def get_feed_data(self, session, feed, hours_past):

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0'
        }
        try:

            async with session.get(feed, headers=headers, timeout=60) as response:

                if response.status != 200:
                    logging.error('feed {} is dead status {} - skip'.format(feed, response.status))
                    return
                # define the root for our parsing
                text = await response.text()

                root = Et.fromstring(text)
                items = root.findall('channel/item')
                for item in items:
                    channel = item.find('title').text
                    pub_date = item.find('pubDate').text
                    title = channel.encode('UTF-8').decode('UTF-8')
                    published = datetime.strptime(pub_date.replace("GMT", "+0000"), '%a, %d %b %Y %H:%M:%S %z')
                    time_between = datetime.now(pytz.utc) - published
                    if time_between.total_seconds() / (60 * 60) <= hours_past:
                        # append the source
                        self.headlines['source'].append(feed)
                        # append the publication date
                        self.headlines['pubDate'].append(pub_date)
                        # append the title
                        self.headlines['title'].append(title)
                        # print(channel)

        except aiohttp.ServerConnectionError as e:
            logging.error(f'Could not parse {feed} error is: {e}')
        except UnicodeDecodeError as e:
            logging.error(f'Could not parse {feed} error is: {e}')
        except AttributeError as e:
            logging.error(f'Could not parse {feed} error is: {e}')
        except ValueError as e:
            logging.error(f'Could not parse {feed} error is: {e}')
        except Et.ParseError as e:
            logging.error(f'Could not parse {feed} error is: {e}')

    async def get_by_csv(self, hours_past):
        with open(self.csv_file) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)
            feeds = []
            for row in csv_reader:
                feeds.append(row[0])

        async with aiohttp.ClientSession() as session:
            tasks = []
            for feed in feeds:
                task = asyncio.ensure_future(self.get_feed_data(session, feed, hours_past))
                tasks.append(task)
            # This makes sure we finish all tasks/requests before we continue executing our code
            await asyncio.gather(*tasks)
            return self.headlines
