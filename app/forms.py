from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','slug', 'content', 'image', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-custom'}),
            'slug': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'id': 'id_slug'}),
            'content': forms.Textarea(attrs={'class': 'form-control form-control-custom', 'rows': 10}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-custom'}),
            'category': forms.Select(attrs={'class': 'form-control form-control-custom'}),

        }