# Main file for the Steely Dan bot
import logging
import time
# Source child functions. 
from get_client import get_client
from get_random_lyric import get_random_lyric
from tweet_lyric import tweet_lyric

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def main():
    client = get_client()

    while True:
        lyric = get_random_lyric(client)
        tweet_lyric(client, lyric)
        logger.info('Waiting')
        time.sleep(3600)
    
    
if __name__ == "__main__":
    main()
    
