from django.contrib.auth.models import User, Permission


def create_user(username='john'):
    change_profile_permission = Permission.objects.get(
        codename='change_profile')
    user = User.objects.create_user(username)
    user.is_staff=True
    user.user_permissions.add(change_profile_permission)
    user.save()
    return user
