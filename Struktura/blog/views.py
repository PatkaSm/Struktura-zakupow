from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from blog.forms import NewPostForm
from blog.models import Post


@login_required(login_url="/")
def newPost_view(request):
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


@login_required(login_url="/")
def blog_view(request):
    posts = Post.objects.filter().order_by('-date_added')
    return render(request, "blog.html", {'all_posts':posts})


@login_required(login_url="/")
def post_details_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post.html", {'post':post})