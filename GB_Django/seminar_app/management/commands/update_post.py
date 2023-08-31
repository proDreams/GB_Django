from django.core.management import BaseCommand

from seminar_app.models import Post


class Command(BaseCommand):
    help = "Update post title by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('title', type=str, help='post title')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        title = kwargs.get('title')
        post = Post.objects.filter(pk=pk).first()
        post.title = title
        post.save()
        self.stdout.write(f'{post}')
