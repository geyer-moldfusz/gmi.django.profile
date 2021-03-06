from django.contrib.auth.models import User, Permission


def create_user(username='john', email=None):
    change_profile_permission = Permission.objects.get(
        codename='change_profile')
    user = User.objects.create_user(username, email=email)
    user.is_staff = True
    user.user_permissions.add(change_profile_permission)
    user.save()
    return user
