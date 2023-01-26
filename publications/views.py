from django.contrib.auth.models import User
from django.forms import Form
from django.shortcuts import render, redirect

from publications.forms import PostForm
from publications.models import Publication, Topics, Comment, PostLike, CommentLike

topics = Topics.objects.all()

# Создаем здесь представления.
def get_publications(request):
    publications = Publication.objects.all()
    print(publications)
    return render(request, "coments/posts.html", {"posts": publications})

def get_publications_topic(request, string):
    topic = Topics.objects.get(name = string)
    print(topic)
    publications = Publication.objects.filter(topics= topic)
    print(publications)
    return render(request, "coments/posts.html", {"posts": publications})

def find_publication(request, number):
    post = Publication.objects.get(pk = number)
    post_like = len(PostLike.objects.filter(like_post = number))
    comment = Comment.objects.filter(post_id=post.id)

    return render(request, "coments/post.html", {"post": post, "comment": comment, "post_like": post_like})


def add_publication(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # print(form)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('/')
    else:
        form = PostForm

    return render(request, "coments/new_page.html", {'form': form})


def delete_publication(request, number):
    post = Publication.objects.get(pk = number)
    post.delete()
    return redirect('/')



