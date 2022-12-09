from django.contrib.auth.models import User
from django.shortcuts import render
from publications.models import Publication, Topics, Comment, PostLike, CommentLike

topics = Topics.objects.all()

# Создаем здесь представления.
def get_publications(request):
    publications = Publication.objects.all()
    return render(request, "coments/posts.html", {"posts": publications})


def find_publication(request, number):
    post = Publication.objects.get(pk = number)
    post_like = len(PostLike.objects.filter(like_post = number))
    comment = Comment.objects.filter(post_id=post.id)

    return render(request, "coments/post.html", {"post": post, "comment": comment, "post_like": post_like})




