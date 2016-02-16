from django.contrib.auth.models import User, Permission
#from django.http import HttpRequest
#
#
#class GetRequest(HttpRequest):
#
#    def __init__(self):
#        super(GetRequest, self).__init__()
#        self.method = 'GET'


def create_user(username='john', email=None):
    change_profile_permission = Permission.objects.get(
        codename='change_profile')
    user = User.objects.create_user(username, email=email)
    user.is_staff=True
    user.user_permissions.add(change_profile_permission)
    user.save()
    return user
