from django.core.management.base import BaseCommand

from twitter_feed.import_tweets import ImportTweets
from twitter_user.models import TwitterUser


class Command(BaseCommand):
    help = 'Import the tweets'

    def handle(self, *args, **options):
        importer = ImportTweets(TwitterUser.objects.all()[0])
        importer.update_tweets()