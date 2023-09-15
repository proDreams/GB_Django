import inspect

from django.db import models
from django.db.models import Manager
from django.urls import reverse


class GameModel(models.Model):
    result = models.CharField(max_length=10,
                              verbose_name='Результат')
    played = models.DateTimeField(auto_now_add=True,
                                  verbose_name='Дата игры')

    objects = Manager()

    def __str__(self):
        return f'Результат игры: {self.result}, время: {self.played}'

    class Meta:
        ordering = ['-played']

    @staticmethod
    def return_last(n):
        return GameModel.objects.all()[:n]


class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=100,
                                 verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Email')
    bio = models.TextField(verbose_name='Биография')
    dob = models.DateField(verbose_name='Дата рождения')
    rating = models.DecimalField(default=5,
                                 verbose_name='Рейтинг',
                                 max_digits=5,
                                 decimal_places=2)

    objects = Manager()

    def get_absolute_url(self):
        return reverse('seminar_app:author_page', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Заголовок')
    post = models.TextField(max_length=1000,
                            verbose_name='Статья')
    publish_date = models.DateField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,
                                 verbose_name='Категория')
    views = models.IntegerField(default=0,
                                verbose_name='Просмотры')
    publish = models.BooleanField(default=False,
                                  verbose_name='Опубликовано?')

    objects = Manager()

    def get_absolute_url(self):
        return reverse('seminar_app:article_page', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.author} - {self.title} - {self.publish}'


class CommentModel(models.Model):
    post = models.ForeignKey('Post',
                             on_delete=models.CASCADE,
                             verbose_name='Статья')
    comment = models.TextField(verbose_name='Добавить комментарий')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлен')

    def __str__(self):
        return f'Комментарий к статье {self.post}'
