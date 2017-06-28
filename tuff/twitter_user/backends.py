from django.contrib.auth.models import User

from twitter_user.models import TwitterUser
from twitter_user import settings

class TwitterBackend(object):
    def authenticate(self, twitter_id=None, username=None, token=None, secret=None):
        # find or create the user
        print "BAAJSJKBSKBSBSHJBJHSBJSHJSBHJ"
        try:
            info = TwitterUser.objects.get(id=twitter_id)
            # make sure the screen name is current
            if info.name != username:
                info.name = username
                info.save()
            user = info.user
        except TwitterUser.DoesNotExist:
            email    = "%s@twitter.com" % username
            user     = User.objects.create_user(settings.USERS_FORMAT % username, email)
            user.save()
            info = TwitterUser(user=user, name=username, id=twitter_id, token=token, secret=secret)
            info.save()
        return user
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None