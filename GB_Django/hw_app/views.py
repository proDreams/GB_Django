import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('<h1>Главная страница!</h1>')


def about(request):
    logger.info('About page accessed')
    return HttpResponse('<h1>Страница обо мне.</h1>')
