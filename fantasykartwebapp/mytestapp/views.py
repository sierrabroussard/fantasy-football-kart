from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def home(request):
    res = requests.get('https://api.sleeper.app/v1/user/731795370941743104')
    return HttpResponse(res.json()['display_name'])