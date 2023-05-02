from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request

# Create your views here.
def home(request):
    return HttpResponse('Welcomme Hoome')

def index(request):
    if request.method=='POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=6c014f82f35f99c3c58f2abfa54f7833').read()
        json_data = json.loads(res)
        data ={
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data ['coord']['lon']) + ' ' +
            str(json_data ['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }

    else:
        city=''
        data={}
    return render(request, 'index.html',{'city':city,'data':data})

