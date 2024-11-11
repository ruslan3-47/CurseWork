from django.http import HttpResponse
from django.shortcuts import render
from .models import Users

# Create your views here.
menu= {"Бронь":"",
       "Номера":"",
       "О сайте":"http://127.0.0.1:8000/about/"}
menu_item = [(key,value) for key,value in menu.items()]
def index(request):
    user = Users.objects.all()
    return render(request, 'core/index.html',{'menu':menu_item,'title':"Главаня старница","user":user})
def rooms(request):
    return HttpResponse(f"<h1> Список комнат. </h1>")
def select_room (request, type_rooms):
    return HttpResponse(f"<h1>{type_rooms}</h1>")
def about(request):
    return  render(request,"core/about.html", {'title':"О сайте"})

