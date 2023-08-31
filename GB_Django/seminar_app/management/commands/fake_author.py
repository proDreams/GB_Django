import random

from django.core.management.base import BaseCommand
from seminar_app.models import Author


class Command(BaseCommand):
    help = "Generate fake authors."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(first_name=f'Author{i}',
                            last_name=f'Surname{i}',
                            email='mail{i}@mail.ru',
                            bio=f'{"a" * 100}',
                            dob='2000-01-01')
            author.save()
