from traceback import print_tb
from django.shortcuts import render
from django.views.generic import TemplateView
from frontend import models as fronend_models
from PIL import Image

# Create your views here.


class Account(TemplateView):
    template_name = "content/account/index.html"


class addItem(TemplateView):
    template_name = "content/add_item.html"


def addItem(request):
    if request.POST:
        data = request.POST
        # data.pop(0)
        title = request.POST["title"]
        price = request.POST["price"]
        category = request.POST["category"]
        description = request.POST["description"]
        images = request.FILES.getlist('file')
        print(images)
        for i in images:
            print(i)

        # print(request.FILES.getlist('file'))
        # images = request.POST['images []']
        # new_images = images.split("_")

        item = fronend_models.products.objects.create(
            title=title,
            price=price,
            category=category,
            thumbnail="none",
            description=description,

        )

        product_id = item.id
        # print(Thumbnail(new_images[0]))

    return render(request, "content/add_item.html")


def Thumbnail(image):
    images = Image.open(image)
    MAX_SIZE = (200, 200)
    images.thumbnail(MAX_SIZE)
    images.save("iamgename.jpg")
    images.show()
    return images
