from django import forms

from analyze_image.models import ImageAnalyze


class ImageForm(forms.ModelForm):

    class Meta:
        model = ImageAnalyze

        fields = ('image',)
