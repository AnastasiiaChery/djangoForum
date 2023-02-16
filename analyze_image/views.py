from PIL import Image, ExifTags
from django.shortcuts import render, redirect
from analyze_image.forms import ImageForm, ImageUpdateForm, ImageUpdateSize, ImageUpdateColor
from analyze_image.list_rgb_matrix import list_color
from analyze_image.models import ImageAnalyze


def upload_image(request):
    images = ImageAnalyze.objects.all().order_by('pk').reverse()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ImageForm

    return render(request, "analyze_image/prew_images.html", {"images": images, 'form': form})


def image_detail(request, number):
    image = ImageAnalyze.objects.get(id = number)
    image_info = Image.open(image.image)
    detail = image_info._getexif()
    detail_dict = {}
    if detail:
        for key, val in detail.items():
            if key in ExifTags.TAGS:
                detail_dict[ExifTags.TAGS[key]] = val

    return render(request, "analyze_image/image_detail.html", {"image_detail": image, 'detail': detail_dict})


def update_image_detail(request, number, tag_name):
    data_image = {'number':number, 'field': tag_name}
    if request.method == 'POST':
        new_data = request.POST.get('info_image')
        update_tag(number, tag_name, new_data)

        return redirect('upload_image')
    else:
        form = ImageUpdateForm
    return render(request, "analyze_image/update_tag.html", {'data_info': data_image, 'form': form})


def update_tag(number, tag_name, new_data):
    try:
        new_data = int(new_data)
    except:
        print('')
    image = ImageAnalyze.objects.get(id=number)
    image_info = Image.open(image.image)
    exif = image_info.getexif()

    for k, v in ExifTags.TAGS.items():
        if v == tag_name:
            key_tag = k

    exif[key_tag] = new_data
    image_info.save(f'{image.image}', exif=exif)


def remove_tag(request, number, tag_name):

    image = ImageAnalyze.objects.get(id=number)
    image_info = Image.open(image.image)
    exif = image_info.getexif()

    for k, v in ExifTags.TAGS.items():
        if v == tag_name:
            key_tag = k
            break

    if key_tag in exif:
        del exif[key_tag]
    image_info.save(f'{image.image}', exif=exif)

    return redirect('upload_image')


def update_color(request, number):
    image_obj = ImageAnalyze.objects.get(id=number)
    image = Image.open(image_obj.image)
    if request.method == 'POST':
        rgb = list_color.get(request.POST.get('color'))

        gray_img = image.convert("RGB", (rgb))
        gray_img.save(f'{image_obj.image}')

        return redirect('upload_image')
    else:
        form = ImageUpdateColor

    return render(request, "analyze_image/update_color.html", {'data_info': number, 'form': form,})


def update_size(request, number):
    image_obj = ImageAnalyze.objects.get(id=number)
    image = Image.open(image_obj.image)
    if request.method == 'POST':

        (left, upper, right, lower) = (request.POST.get('left'), request.POST.get('upper'), request.POST.get('right'), request.POST.get('lower'))
        (width, height) = (request.POST.get('width'), request.POST.get('height'))

        try:
            image = image.crop((int(left), int(upper), int(right), int(lower)))
            image.save(f'{image_obj.image}')
        except:
            print('ok')

        try:
            image = image.resize((int(width), int(height)))
            image.save(f'{image_obj.image}')
        except:
            print('ok')

        return redirect('upload_image')
    else:
        form = ImageUpdateSize
        current_size = {'width': image.width, 'height': image.height}

    return render(request, "analyze_image/update_size.html", {'data_info': number, 'form': form, 'current_size': current_size})


def delete_image(request, number):
    image = ImageAnalyze.objects.get(pk = number)
    image.delete()
    return redirect('upload_image')