from django.shortcuts import render
from django.http import HttpResponse
import datetime as datetime_lib

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime_lib.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime_lib.datetime.now() + datetime_lib.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset': dt})

