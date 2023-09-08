import inspect

from django.db import models
from django.db.models import Manager
from django.urls import reverse


class GameModel(models.Model):
    result = models.CharField(max_length=10)
    played = models.DateTimeField(auto_now_add=True)

    objects = Manager()

    def __str__(self):
        return f'Результат игры: {self.result}, время: {self.played}'

    class Meta:
        ordering = ['-played']

    @staticmethod
    def return_last(n):
        return GameModel.objects.all()[:n]


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    dob = models.DateField()

    objects = Manager()

    def get_absolute_url(self):
        return reverse('seminar_app:author_page', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=1000)
    publish_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    objects = Manager()

    def get_absolute_url(self):
        return reverse('seminar_app:article_page', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.author} - {self.title} - {self.publish}'
