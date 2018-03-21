from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    #here is the relationship with the users

    user = models.OneToOneField(User)

    ##just additional alttributes to our class
    portfolio_site = models.URLField(blank=True)

    # we need to: pip install pillow  to work this imagefield

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):

        # notice that the username is a built-in django class User

        return self.user.username
