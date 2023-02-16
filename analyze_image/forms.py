from django import forms

from analyze_image.models import ImageAnalyze

choises =(("blue", "Blue"),
    ("yellow", "Yellow"),
    ("green", "Green"),
    ("warm", "Warm"),
    ("pink", "Pink"),
    ("dark", "Dark"),
)

class ImageForm(forms.ModelForm):

    class Meta:
        model = ImageAnalyze

        fields = ('image',)

class ImageUpdateForm(forms.Form):
    info_image = forms.TimeField()


class ImageUpdateSize(forms.Form):
    width = forms.IntegerField(required= False)
    height = forms.IntegerField(required= False)

    left = forms.IntegerField(required= False)
    upper = forms.IntegerField(required= False)
    right = forms.IntegerField(required= False)
    lower = forms.IntegerField(required= False)


class ImageUpdateColor(forms.Form):
    color = forms.ChoiceField(choices=choises)


