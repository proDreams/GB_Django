from django.core.management import BaseCommand

from seminar_app.models import Post


class Command(BaseCommand):
    help = 'Get all posts'

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()

        self.stdout.write(f'{posts}')