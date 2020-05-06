from django import forms

from blog.models import Post
from blog.models import Todo


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class TaskForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('task',)
        widgets = {
            'task': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

