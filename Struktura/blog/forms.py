from django import forms
from blog.models import Post, Comment


class NewPostForm(forms.ModelForm):
    title = forms.CharField(label="")
    content = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Post
        fields = ['title', 'content']


class NewCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label="")

    class Meta:
        model = Comment
        fields = ['content']