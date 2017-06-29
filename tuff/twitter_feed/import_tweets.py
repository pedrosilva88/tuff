import tweepy
import traceback
from django.conf import settings
from django.db import transaction

from twitter_feed.models import Tweet
from twitter_user.models import TwitterUser


class ImportTweets:

    def __init__(self, twitterUser):
        self.consumer_key = settings.TWITTER_KEY
        self.consumer_secret = settings.TWITTER_SECRET
        self.o_auth_token = twitterUser.oauth_token
        self.o_auth_secret = twitterUser.oauth_secret

    def update_tweets(self):
        raw_tweets = self._get_latest_tweets_from_api()
        tweets = [self._tweepy_status_to_tweet(status=status) for status in raw_tweets]
        self._replace_all_tweets(tweets)

    def _get_latest_tweets_from_api(self):
        """
        http://pythonhosted.org/tweepy/html/index.html
        """
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.o_auth_token, self.o_auth_secret)
        api = tweepy.API(auth)

        return api.home_timeline()

    def _tweepy_status_to_tweet(self, status):
        """
        Fields documentation: https://dev.twitter.com/docs/api/1.1/get/statuses/home_timeline
        """
        tweet = Tweet()
        tweet.published_at = status.created_at
        tweet.content = status.text

        return tweet

    @transaction.atomic
    def _replace_all_tweets(self, new_tweets):
        try:
            with transaction.atomic():
                Tweet.objects.remove_all()

                for tweet in new_tweets:
                    tweet.save()

                #transaction.commit()
        except Exception:
            traceback.print_exc()
            pass