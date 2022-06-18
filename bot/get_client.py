#!/usr/bin/env python
# Python Script for getting client variables
import tweepy
import os
import logging

logger = logging.getLogger()

def get_client():
    bearer_token = os.getenv("BEARER_TOKEN")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    
    client = tweepy.Client(bearer_token, consumer_key, consumer_secret,
                           access_token, access_token_secret,
                           wait_on_rate_limit=True)
    
    try:
        me = client.get_me()
        print(me)
    except Exception as e:
        logger.error("Error getting client", exc_info=True)
        raise e
    
    logger.info("Client successfully created.")
    return client