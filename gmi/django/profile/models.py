from django.contrib.auth.models import User
from django.db import models

import gmi.django.avatar.utils as avatar_utils

class Profile(models.Model):
    user = models.OneToOneField(User)
    about = models.TextField()

    @property
    def avatar_url(self):
        return avatar_utils.get_avatar_url(self.user.email, 160)
