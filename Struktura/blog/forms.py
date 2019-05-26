from django import forms
from blog.models import Post, Comment


class NewPostForm(forms.ModelForm):
    title = forms.CharField(label="Tytuł posta")
    content = forms.CharField(widget=forms.Textarea, label="Treść posta")

    class Meta:
        model = Post
        fields = ['title', 'content']


class NewComentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label="Treść komentarza")

    class Meta:
        model = Comment
        fields = ['content']