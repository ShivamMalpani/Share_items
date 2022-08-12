from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# rooms = [
#     {'id':1,'name':'Be consistent'},
#     {'id':2, 'name': 'Be productive'},
# ]

def home(request):
    rooms = Room.objects.all()
    # for i in rooms:
    #     room = i
    context = {'room':rooms}
    return render(request,'base/home.html',context)

# rooms = [{'id':3, 'name':'Frontend'},{'id':2,'name':'Backend'},{'id':1,'name':'DSA'}]
def room(request, pk):
    rooms = Room.objects.all()
    # print(pk)
    room = None
    for i in rooms:
        # print(i.id)
        if i.id == int(pk):
            # print(i)
            room = i
    # room = Room.objects.get(id = pk)
    context = {'room':room}
    return render(request,'Room.html',context)

def createRoom(request):
    # room = Room.objects.all()
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form': form}
    return render(request,'base/create_room.html',context)

def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    print(room)
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base/home.html')
    context = {'room': room}
    return render(request,'base/update.html',context)