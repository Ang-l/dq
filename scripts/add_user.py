from user.models import Users


def run():
    for i in Users.objects.all():
        print(i.username)