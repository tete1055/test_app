from django.forms import ModelForm
from .models import Post, Good
from django import forms

# class PostForm(ModelForm):
#     '''
#     '''
#     class Meta:
#         '''
#         Attributes:
#           model:
#           fields:
#         '''
#         model = Post
#         fields = ['content']

class GoodForm(ModelForm):
    class Meta:
        model = Good
        fields = ['owner', 'post']

class CreatePostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())

# class CreatePostForm(forms.Form):
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': '60', 'rows': '10'}))
