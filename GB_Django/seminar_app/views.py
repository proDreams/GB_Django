from random import randint

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView

from seminar_app import models, forms
from seminar_app.models import GameModel, Author, Post
from seminar_app.forms import ChooseGameForm


def index(request):
    context = {
        'title': 'Главная страница',
        'data': 'Текст главной страницы'
    }

    return render(request,
                  'seminar_app/index.html',
                  context)


def about(request):
    context = {
        'title': 'Главная страница',
        'data': 'Текст страницы о нас'
    }

    return render(request,
                  'seminar_app/about.html',
                  context)


class GameView(TemplateView):
    template_name = 'seminar_app/game.html'


class HeadsGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [('TAILS', 'HEADS')[randint(0, 1)] for i in range(self.kwargs['count'])]
        context['results'] = results
        context['title'] = 'Игра в Орла и Решку'
        return context


class DiceGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [randint(0, 6) for i in range(self.kwargs['count'])]
        context['results'] = results
        context['title'] = 'Игра в кости'
        return context


class AllArticlesView(TemplateView):
    template_name = 'seminar_app/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['pk'])
        posts = Post.objects.filter(author=author).all()
        context['posts'] = posts
        context['title'] = f'Посты автора {author}'
        return context


class ArticlePage(DetailView):
    model = Post
    template_name = 'seminar_app/article_page.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj


def heads(request):
    result = ('TAILS', 'HEADS')[randint(0, 1)]

    game = GameModel(result=result)
    game.save()

    return HttpResponse(f'{game}')


def last_games(request):
    last = GameModel().return_last(5)
    last_str = ['<br>' + str(i) for i in last]
    return HttpResponse(last_str)


def authors(request):
    res = Author.objects.all()
    print(res)
    res1 = ''
    for i in res:
        res1 += str(i) + '<br>'
    return HttpResponse(f'{res1}')


class AddAuthor(CreateView):
    model = models.Author
    template_name = 'seminar_app/add_author.html'
    form_class = forms.AddAuthorForm


class AuthorPage(DetailView):
    model = models.Author
    template_name = 'seminar_app/author_page.html'


class AddPost(CreateView):
    model = models.Post
    template_name = 'seminar_app/add_post.html'
    form_class = forms.AddPostForm


class Games(TemplateView):
    template_name = 'seminar_app/game_choose.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ChooseGameForm()
        context['results'] = kwargs.get('results', [])
        return context

    def post(self, request, *args, **kwargs):
        form = ChooseGameForm(request.POST)
        results = []
        if form.is_valid():
            match form.cleaned_data.get('game'):
                case 'dice':
                    for _ in range(form.cleaned_data.get('count')):
                        results.append(randint(1, 6))
                case 'rand_number':
                    for _ in range(form.cleaned_data.get('count')):
                        results.append(randint(1, 1000))
                case 'heads_tails':
                    for _ in range(form.cleaned_data.get('count')):
                        results.append(('TAILS', 'HEADS')[randint(0, 1)])
        return self.get(request, *args, **kwargs, results=results)
