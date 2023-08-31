from django.urls import path

from seminar_app import views

app_name = 'seminar_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('last/', views.last_games, name='last_games'),
    path('author/', views.autor, name='author'),
]
