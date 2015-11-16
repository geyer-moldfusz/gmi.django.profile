from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django_markdown.admin import MarkdownInlineAdmin

from gmi.django.profile.models import Profile


class ProfileInline(MarkdownInlineAdmin):
    model = Profile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
