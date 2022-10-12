from random import Random, random
from django.views.generic import TemplateView
from frontend import models as fronend_models
from PIL import Image
import os
import uuid
from happydoll.settings import BASE_DIR
from django.shortcuts import render


# Create your views here.


class Account(TemplateView):
    template_name = "content/account/index.html"


class addItem(TemplateView):
    template_name = "content/add_item.html"


def addItem(request):
    if request.POST:
        data = request.POST
        path = os.path.join(BASE_DIR, "MEDIA/thumbnail/")
        # data.pop(0)
        title = request.POST["title"]
        price = request.POST["price"]
        category = request.POST["category"]
        description = request.POST["description"]
        images = request.FILES.getlist('file')
        # print(images)

        urls = []
        # creating image thumbnail
        if images is not None:
            for index, image in enumerate(images):
                thumbnail = Thumbnail(image, path)
                urls.append(thumbnail)

        images_url = f"{urls[0]} {urls[1]} {urls[2]} {urls[4]}"
        slug = title.replace(" ", "-")
        # slug += Random.randint(1, 200000000)

        item = fronend_models.products.objects.create(
            title=title,
            price=price,
            category=category,
            description=description,
            thumbnail=images_url,
            slug=slug


        )

        for i in images:
            fronend_models.images.objects.create(
                products=item,
                images=i
            )

    return render(request, "content/add_item.html")


def Thumbnail(image, path):
    images = Image.open(image)
    MAX_SIZE = (300, 300)
    images.thumbnail(MAX_SIZE)
    image_name = f"{uuid.uuid4()}thumbnail.webp"

    full_name = f"{path}/{image_name}"
    # imag
    images.save(full_name)
    # images.show()
    return image_name
