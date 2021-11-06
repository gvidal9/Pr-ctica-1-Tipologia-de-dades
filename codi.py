#https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1
#https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/tweet
#https://docs.tweepy.org/en/latest/api.html#API.search

import tweepy
import pandas
import time

consumer_key = "4ikBRcdJVZJmcXF8WOsuQ0VY5"
consumer_secret = "ksmxgT77nUprvScPsPqb3bgy387cLkuTaiIMmqsKfsOcoA5Bbh"
access_token = "1455605536582512643-zJ9scn7mf8WYmNca2DB90cNLHYVC8P"
access_token_secret = "ZLuoquSYSjEyUVzKxDFlLoSkGG9588Ee7ZCftqCQZhoeM"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Utiltzem la paraula brexit per filtrar i cerquem les darreres 1000 opinions.
text_query = 'brexit'
count = 1000
try:
    tweets = tweepy.Cursor(api.search_tweets, q=text_query).items(count)

    
    tweets_list = [[tweet.created_at,
                    tweet.id,
                    tweet.text,
                    tweet.truncated,
                    tweet.in_reply_to_screen_name,
                    tweet.place,
                    tweet.is_quote_status,
                    tweet.retweeted] for tweet in tweets]

    # Creació del df per ordenar la informació
    # Add or remove columns as you remove tweet information
    tweets_df = pandas.DataFrame(tweets_list)

except BaseException as e:
    print('failed on_status,', str(e))
    time.sleep(3)

#Escriure el directori on volem guardar el document
tweets_df.to_csv(r'C:\Users\Guillem\Desktop\Màster\3r semestre\Tipologia de dades\dataset.csv')
