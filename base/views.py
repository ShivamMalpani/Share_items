from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Room

rooms = [
    {'id':1,'name':'Be consistent'},
    {'id':2, 'name': 'Be productive'},
]

def home(request):
    rooms = Room.objects.all()
    for i in rooms:
        print(i)
    context = { 'rooms':rooms}
    return render(request,'base/home.html',context)


def room(request, pk):
    print(pk)
    room = Room.objects.get(id = pk)
    context = {'room':room}
    return render(request,'Room.html',context)
