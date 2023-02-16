from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from publications.forms import PostForm, CommentForm
from publications.models import Publication, Topics, Comment, PostLike



def get_publications(request):
    publications = Publication.objects.all()
    return render(request, "coments/posts.html", {"posts": publications})


def get_publications_topic(request, string):
    topic = Topics.objects.get(name = string)
    publications = Publication.objects.filter(topics= topic)
    return render(request, "coments/posts.html", {"posts": publications})


def find_publication(request, number):
    post = Publication.objects.get(pk = number)
    post_like = len(PostLike.objects.filter(like_post = number))
    comment = Comment.objects.filter(post_id=post.id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            data.post = post
            data.save()
    else:
        form = CommentForm

    return render(request, "coments/post.html", {"post": post, "comment": comment, "post_like": post_like, 'form': form})


def like_publication(request, number):
    post = Publication.objects.get(pk=number)
    current_user = request.user
    find_post = PostLike.objects.filter(author=current_user.id, like_post = post)

    if find_post:
        find_post.delete()
    else:
        user = User.objects.get(pk=current_user.id)
        new_like = PostLike.objects.create()
        new_like.like_post.set([post])
        new_like.author.set([user])

    return redirect('/post/{}'.format(number))


def add_publication(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm

    return render(request, "coments/new_page.html", {'form': form})


def delete_publication(request, number):
    post = Publication.objects.get(pk = number)
    post.delete()
    return redirect('post_list')

