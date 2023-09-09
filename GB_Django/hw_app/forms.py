from django import forms

from hw_app import models


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['title', 'description', 'price', 'count', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
