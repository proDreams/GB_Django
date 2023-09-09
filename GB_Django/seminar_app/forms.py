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


class ChooseGameForm(forms.Form):
    game = forms.ChoiceField(
        choices=[('dice', 'Dice'), ('rand_number', 'Random Number'), ('heads_tails', 'Heads or Tails')],
        widget=forms.Select(attrs={'class': 'form-select'}))
    count = forms.IntegerField(min_value=1,
                               max_value=64,
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))


class AddCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = models.CommentModel
        fields = ['comment']
