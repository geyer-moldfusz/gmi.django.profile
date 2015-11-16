from django.contrib.auth.models import User
from django_markdown.models import MarkdownField
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    about = MarkdownField()

    @property
    def name(self):
        if self.user.first_name:
            if self.user.last_name:
                return '{} {}'.format(
                    self.user.first_name, self.user.last_name)
            return self.user.first_name
        return self.user.username
