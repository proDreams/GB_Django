from django import forms

from seminar_app import models


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['first_name', 'last_name', 'email', 'bio', 'dob']


class AddPostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'post', 'author', 'category']