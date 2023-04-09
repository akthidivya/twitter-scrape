import snscrape.modules.twitter as sntwitter
from datetime import datetime


"""
Scrape the twitter feeds with details
Example input for query parameter: "COVID Vaccine since:2021-01-01 until:2021-05-31"
"""

def scrape_twitter(query):
    # Try exception block to handle the exceptions
    try:
        # Creating list to append tweet data to
        tweets_list = []

        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            # Set the count to limit the scrape data
            if i>100:
                break
            tweets_list.append([tweet.date, int(tweet.id), str(tweet.content), str(tweet.url), str(tweet.user), int(tweet.replyCount), int(tweet.retweetCount), str(tweet.lang), str(tweet.source), int(tweet.likeCount)])

        return tweets_list
    
    except Exception as e:
        print(e)
        return False
