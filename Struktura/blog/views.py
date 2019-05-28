from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from blog.forms import NewPostForm, NewCommentForm
from blog.models import Post, Comment


@login_required(login_url="/")
def newPost_view(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = NewPostForm(request.POST or None)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.date_added = timezone.now()
                post.save()
                return redirect('blog')
        else:
            form = NewPostForm()
        return render(request, "new_post.html", {'post_form':form})
    else:
        raise Http404("Nie możesz tego oglądać")


@login_required(login_url="/")
def blog_view(request):
    if request.method == 'POST' and 'post_id' in request.POST:
        delete_post = get_object_or_404(Post, id=request.POST['post_id'])
        delete_post.delete()
        posts = Post.objects.filter().order_by('-date_added')
        return render(request, "blog.html", {'all_posts': posts})
    else:
        posts = Post.objects.filter().order_by('-date_added')
    return render(request, "blog.html", {'all_posts':posts})


@login_required(login_url="/")
def post_details_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = NewCommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.date_added = timezone.now()
            comment.post = post
            comment.save()
            comments = Comment.objects.filter(post = post)
            form = NewCommentForm(request.POST or None)
            return render(request, "post.html", {'post': post, 'comment_form':form, 'comments':comments})
    else:
        form = NewCommentForm(request.POST or None)
        comments = Comment.objects.filter(post=post)
    return render(request, "post.html", {'post':post,'comment_form':form, 'comments':comments})