from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.

def index(request):
    response = requests.get('http://myapi:8000')
    print(response)
    data = response.json()
    name = data['user']
    message = data['message']

    return HttpResponse('<h2> {} </h2> <h5> {} </h5>'.format(name, message))