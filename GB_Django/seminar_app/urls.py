from django.urls import path

from seminar_app import views

app_name = 'seminar_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('heads_game/<int:count>', views.HeadsGame.as_view(), name='heads_game'),
    path('dice_game/<int:count>', views.DiceGame.as_view(), name='dice_game'),
    path('articles/<int:pk>', views.AllArticlesView.as_view(), name='articles'),
    path('article/<int:pk>', views.ArticlePage.as_view(), name='article_page'),
    path('heads/', views.heads, name='heads'),
    path('last/', views.last_games, name='last_games'),
    path('author/', views.authors, name='author'),
    path('add_author/', views.AddAuthor.as_view(), name='add_author'),
    path('author_page/<int:pk>', views.AuthorPage.as_view(), name='author_page'),
    path('article/add', views.AddPost.as_view(), name='add_post'),
]
