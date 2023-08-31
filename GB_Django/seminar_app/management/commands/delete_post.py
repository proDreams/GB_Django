from django.core.management import BaseCommand

from seminar_app.models import Post


class Command(BaseCommand):
    help = "Delete post title by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        post = Post.objects.filter(pk=pk).first()
        post.delete()
        self.stdout.write(f'Deleted {post}')
