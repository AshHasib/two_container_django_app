from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def index(request):

    data = {
        'user': 'AshHasib',
        'message':'This message has come from an API'
    }

    return HttpResponse(json.dumps(data), content_type = 'application/json')