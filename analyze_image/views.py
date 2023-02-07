from PIL import Image, ExifTags
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.templatetags import static
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from analyze_image.forms import ImageForm
from analyze_image.models import ImageAnalyze


def upload_image(request):
    images = ImageAnalyze.objects.all()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
            # print(form)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ImageForm

    return render(request, "analyze_image/prew_images.html", {"images": images, 'form': form})

def image_detail(request, number):
    image = ImageAnalyze.objects.get(id = number)
    image_info = Image.open(f'static/{image.image}')
    detail = image_info._getexif()
    detail_dict ={}
    for key, val in detail.items():
        if key in ExifTags.TAGS:
            detail_dict[ExifTags.TAGS[key]]= val

    # print(exif)
    return render(request, "analyze_image/image_detail.html", {"image_detail": image, 'detail': detail_dict })


def delete_image(request, number):
    image = ImageAnalyze.objects.get(pk = number)
    image.delete()
    return redirect('upload_image')