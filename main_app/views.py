from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Fan, World_Cup
from .forms import FanForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    context = {'cup': world_cup, 'fan_form': fan_form}
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