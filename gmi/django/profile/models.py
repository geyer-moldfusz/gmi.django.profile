from django.contrib.auth.models import User
from django.db import models

import gmi.django.avatar.utils as avatar_utils

class Profile(models.Model):
    user = models.OneToOneField(User)
    about = models.TextField()
