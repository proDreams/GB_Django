import random

from django.core.management.base import BaseCommand
from seminar_app.models import Post, Author, Category


class Command(BaseCommand):
    help = "Generate fake authors."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for c in Category.objects.all():
            for a in Author.objects.all():
                for i in range(1, count + 1):
                    post = Post(title=f'title{i}',
                                post=f'post{i}',
                                publish_date='2000-01-01',
                                # author=random.randint(1, 7),
                                author=a,
                                category=c,
                                views=random.randint(1, 1000),
                                publish=random.randint(0, 1))
                post.save()
