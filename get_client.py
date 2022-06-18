#!/usr/bin/env python
# Python Script for getting client variables
import tweepy
import os
import logging

logger = logging.getLogger()

# TODO: remove this once finished. 
# For testing
# os.environ["BEARER_TOKEN"] = "AAAAAAAAAAAAAAAAAAAAAEabdwEAAAAANGcnWgsfrtyu5nSVdgEKHB1bJgg%3DCjDwlySuwoOyxCg6CmtAP3E93VsAanODrYVNTcJnUsKvUlFHyk"
# os.environ["CONSUMER_KEY"] = "0JYo3LIT2F8oaPj60wMsks5a1"
# os.environ["CONSUMER_SECRET"] = "oZ2b9GpfzmtJXDCgyYyFNIp8juN8eMSv5DCj8ESo33F7VMBj4Y"
# os.environ["ACCESS_TOKEN"] = "478198693-7os66GWhx6GrTU7UPbIldCHQG7h7baQ8ipJuzelT"
# os.environ["ACCESS_TOKEN_SECRET"] = "R6MtmAw15mAeyUBWf5fGDfMbib7uCrfhKhmWmpQ2q0Uf9"

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