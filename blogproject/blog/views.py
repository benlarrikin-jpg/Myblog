from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

# Create your views here.

def blog_list(request):
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-created_on')
    request.method == 'POST'

    form = CommentForm(request.POST)
    if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('blog_detail', slug=comments.post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
})