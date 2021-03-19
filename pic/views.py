from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Picture

# Create your views here.

def pic(request):
    date = dt.date.today()
    pic = Picture.ft_pic()
    return render(request, 'pic.html', {"date": date,"pic":pic})


def picture(request,picture_id):
    try:
        picture = Picture.objects.get(id = picture_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"article.html", {"picture":picture})
