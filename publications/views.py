from django.contrib.auth.models import User
from django.forms import Form
from django.shortcuts import render, redirect

from publications.forms import PostForm, CommentForm
from publications.models import Publication, Topics, Comment, PostLike, CommentLike



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
    comment_like_count = {}
    for i in comment:
        comment_like = len(CommentLike.objects.filter(like_comment=i.id))
        comment_like_count[i.id] = comment_like

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            data.post = post
            data.save()
            # return redirect('/')
    else:
        form = CommentForm
        print(form)

    return render(request, "coments/post.html", {"post": post, "comment": comment, "post_like": post_like, "comment_like": comment_like_count, 'form': form})


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
        # new_like.save()

    return redirect('/post/{}'.format(number))


def like_comment(request, number):
    comment = Comment.objects.get(pk=number)
    current_user = request.user
    find_post = CommentLike.objects.filter(author=current_user.id, like_comment = comment)

    if find_post:
        find_post.delete()
    else:
        user = User.objects.get(pk=current_user.id)
        new_like = CommentLike.objects.create()
        new_like.like_comment.set([comment])
        new_like.author.set([user])
        # new_like.save()

    return redirect('/post/{}'.format(comment.post.id))

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
    return redirect('/')



# Analyze Image