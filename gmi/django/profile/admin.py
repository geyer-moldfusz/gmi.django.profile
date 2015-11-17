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


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('about',)
    exclude = ('user',)
    list_display = ('name',)

    def has_change_permission(self, request, profile=None):
        if not profile or request.user.is_superuser:
            return super(ProfileAdmin, self).has_change_permission(
                request, profile)
        if request.user == profile.user:
            return True
        return False

    def get_queryset(self, request):
        qs = super(ProfileAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
