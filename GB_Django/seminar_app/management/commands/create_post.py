import random

from django.core.management.base import BaseCommand
from seminar_app.models import Post, Author, Category


class Command(BaseCommand):
    help = "Create post."

    def add_arguments(self, parser):
        parser.add_argument('author', type=int, help='author ID')
        parser.add_argument('category', type=int, help='category ID')

    def handle(self, *args, **kwargs):
        author = Author.objects.get(pk=kwargs.get('author'))
        category = Category.objects.get(pk=kwargs.get('category'))

        post = Post(title=f'title',
                    post=f'post',
                    publish_date='2000-01-01',
                    author=author,
                    category=category,
                    views=random.randint(1, 1000),
                    publish=random.randint(0, 1))

        post.save()

        self.stdout.write(f'done, post pk = {post.pk}')
