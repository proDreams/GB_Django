from django.core.management import BaseCommand

from lecture_app.models import User


class Command(BaseCommand):
    help = 'Create user.'

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        # user = User(name='Neo', email='neo@example.com', password='secret', age=58)
        user = User(name='Jack', email='captain@example.com', password='secret', age=60)

        user.save()
        self.stdout.write(f'{user}')
