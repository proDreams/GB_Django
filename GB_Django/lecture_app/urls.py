from django.urls import path

from . import views

app_name = 'lecture_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user_form/', views.user_form, name='user_form'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_user_class/', views.AddUser.as_view(), name='add_user_class'),
    path('many_fields_form/', views.many_fields_form, name='many_fields_form'),
]
