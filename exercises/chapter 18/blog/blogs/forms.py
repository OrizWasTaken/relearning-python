from django import forms
from .models import Blog, Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']
        labels = {'title': 'Title', 'description': 'Description'}
        widgets = {
            'title': forms.TextInput(attrs={'style': 'display:block; width:350px'}),
            'description': forms.Textarea(attrs={'cols': 80, 'style': 'display:block'})
            }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        labels = {'title': 'Title', 'text': 'Content'}
        widgets = {
            'title': forms.TextInput(attrs={'style': 'display:block; width:350px'}),
            'text': forms.Textarea(attrs={'rows': 20, 'cols': 80, 'style': 'display:block'})
            }