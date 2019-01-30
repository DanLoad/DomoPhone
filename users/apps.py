from django.apps import AppConfig

tests()

class UsersConfig(AppConfig):
    name = 'users'


def tests():
    print("ok ok ok")
