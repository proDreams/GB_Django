from django.core.management import BaseCommand

from lecture_app.models import Author, Post


class Command(BaseCommand):
    help = "Get all posts by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = f'\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')

    # def handle(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     author = Author.objects.filter(pk=pk).first()
    #     if author is not None:
    #         posts = Post.objects.filter(author=author)
    #         intro = f'All posts of {author.name}\n'
    #         text = f'\n'.join(post.content for post in posts)
    #         self.stdout.write(f'{intro}{text}')
