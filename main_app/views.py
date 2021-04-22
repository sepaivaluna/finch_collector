from django.shortcuts import render, redirect
import uuid
import boto3
from .models import Photo, World_Cup, FanAttire
from .forms import FanForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

S3_BASE_URL = "https://s3-us-east-2.amazonaws.com/"
BUCKET = "actualworldcup"

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def worldcups_index(request):
    world_cups = World_Cup.objects.all()
    context = {'world_cups': world_cups}
    return render(request, 'world_cups/index.html', context)


def worldcups_details(request, cup_id):
    world_cup = World_Cup.objects.get(id=cup_id)
    fan_form = FanForm()
    attire_world_cup_fans = FanAttire.objects.exclude(
        id__in=world_cup.fan_attire.all().values_list('id'))
    context = {
        'cup': world_cup,
        'fan_form': fan_form,
        'items': attire_world_cup_fans
    }
    return render(request, 'world_cups/detail.html', context)


class CupCreate(CreateView):
    model = World_Cup
    fields = '__all__'


class CupUpdate(UpdateView):
    model = World_Cup
    fields = ['location', 'year', 'mvps']


class CupDelete(DeleteView):
    model = World_Cup
    success_url = '/world_cups/'


def add_fan(request, cup_id):
    form = FanForm(request.POST)
    if form.is_valid():
        new_fan = form.save(commit=False)
        new_fan.world_cup_id = cup_id
        new_fan.save()
    return redirect('detail', cup_id=cup_id)


def items_index(request):
    items = FanAttire.objects.all()
    context = {"items": items}

    return render(request, "item/index.html", context)


def item_detail(request, item_id):
    item = FanAttire.objects.get(id=item_id)
    context = {"item": item}
    return render(request, "item/detail.html", context)


class Create_item(CreateView):
    model = FanAttire
    fields = "__all__"


class Update_item(UpdateView):
    model = FanAttire
    fields = ["clothing", 'description']


class Delete_item(DeleteView):
    model = FanAttire
    success_url = "/items/"


def assoc_attire(request, cup_id, item_id):
    World_Cup.objects.get(id=cup_id).fan_attire.add(item_id)
    return redirect('detail', cup_id=cup_id)


def add_photo(request, cup_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get("photo-file", None)
    if photo_file:
        s3 = boto3.client("s3")
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind("."
                                                                           ):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, world_cup_id=cup_id)
            photo.save()
        except:
            print("An error occurred uploading file to S3")
    return redirect("detail", cup_id=cup_id)
