from django.contrib.auth.models import Group


def new_users_handler(backend, user, response, *args, **kwargs):
    group = Group.objects.filter(name='social')
    group_custom = Group.objects.get(name='custom')
    if len(group):
        user.groups.add(group[0])
        user.groups.add(group_custom)

