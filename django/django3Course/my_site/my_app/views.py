from datetime import date
from django.shortcuts import render
from django.http.response import HttpResponse
from my_app.models import Topic, Webpage, AccessRecord
# Create your views here.


def simple_views(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dict = {'insert_me': "Hello this is views.py"}
    return render(request, 'my_app/index.html', context=date_dict)
