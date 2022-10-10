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
        print(path)
        # data.pop(0)
        title = request.POST["title"]
        price = request.POST["price"]
        category = request.POST["category"]
        description = request.POST["description"]
        images = request.FILES.getlist('file')
        # print(images)

        item = fronend_models.products.objects.create(
            title=title,
            price=price,
            category=category,
            description=description,

        )

        # product_id = item.id
        thumbnail_url = []
        for index, image in enumerate(images, start=1):
            thumbnail = Thumbnail(image, path)
            thumbnail_url.append(thumbnail)
            if index == 2:
                break
        for i in images:
            fronend_models.images.objects.create(
                products=item,
                thumbnail=f"{thumbnail_url[0]} {thumbnail_url[1]}",
                images=i
            )

    return render(request, "content/add_item.html")


def Thumbnail(image, path):
    images = Image.open(image)
    MAX_SIZE = (500, 400)
    images.thumbnail(MAX_SIZE)
    image_name = f"{uuid.uuid4()}thumbnail.webp"

    full_name = f"{path}/{image_name}"
    # imag
    images.save(full_name)
    # images.show()
    return image_name
