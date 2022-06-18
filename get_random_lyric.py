#!/usr/bin/env python
# Function that gets a random lyric from text file, checks against
# previously tweeted lyrics, and returns lyric if it hasn't been tweeted in
# the past 7 days.

import logging
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# For testing = 
def get_random_lyric(client):
    RANDOM_LYRIC_LOOP = True
    while RANDOM_LYRIC_LOOP:
        # Read in lyrics txt file 
        f = open("lyrics.txt", "r")
        lyrics = f.read().splitlines()
        f.close()
    
        random_lyric = random.choice(lyrics)
        print(random_lyric)
    
        # Compare random lyric to previous tweets
        userInfo = dict(client.get_me()[0])
        username = userInfo['username']
        searchQuery = 'from:' + username + " \"" + random_lyric + "\""
        lyrics_exists = dict(client.search_recent_tweets(query = searchQuery)[3])['result_count']
        if(lyrics_exists == 0):
            RANDOM_LYRIC_LOOP = False
        
    return(random_lyric)

        
    
    
    