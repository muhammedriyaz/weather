from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
import requests
import json

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"

def getWeatherData(request):
    apiKey = 'your-api-key-here'
    city   = request.POST['city']
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid='+apiKey)
    data = res.json()
    temperature = data['main']['temp']
    city_name   = data['name']
    response = {}
    response['weather'] = temperature
    response['error']   = "It's "+str(temperature)+" ℃ in "+city_name
    return JsonResponse(response)