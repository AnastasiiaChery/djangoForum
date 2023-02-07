from django import forms

from publications.models import Publication, Topics, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Publication

        fields = ('text', 'image', 'topics', 'author')

        # print(topics.queryset)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ('comment', 'post', 'author')


