#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def tweet_lyric(client, lyric):
    logger.info('Tweeting random lyric.')
    client.create_tweet(text=lyric)