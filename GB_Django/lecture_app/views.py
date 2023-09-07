import logging
from audioop import reverse

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from lecture_app.forms import UserForm, ManyFieldsForm
from lecture_app.models import UserModel

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Hello, world!')


def about(request):
    try:
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse('Oops, something went wrong.')
    else:
        logger.debug('About page accessed')
        return HttpResponse('This is the about page')


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}')
    else:
        form = UserForm()
    return render(request,
                  'lecture_app/user_form.html',
                  {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}')
    else:
        form = ManyFieldsForm()
    return render(request,
                  'lecture_app/many_fields_form.html',
                  {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}')
            user = UserModel(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request,
                  'lecture_app/user_form.html',
                  {'form': form, 'message': message})


class AddUser(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = 'lecture_app/user_form.html'
    success_url = '/'
