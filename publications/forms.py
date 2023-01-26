from django import forms

from publications.models import Publication, Topics


class PostForm(forms.ModelForm):
    # topics = forms.ModelMultipleChoiceField(
    #     queryset=Topics.objects.all().values(),
    #     widget=forms.CheckboxSelectMultiple
    # )
    class Meta:
        model = Publication

        fields = ('text', 'image', 'topics', 'author')

        # print(topics.queryset)

