from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('published_date', 'user')


class UpdateFileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')




