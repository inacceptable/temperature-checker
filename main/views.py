import requests
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from datetime import date
import calendar
def index(request):
	apidata = requests.get('https://api.openweathermap.org/data/2.5/weather?q=melbourne,3000,australia&appid=df584a0437488bfbfafc54efe54ddced&units=metric').json()
	apidata_7day = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=-37.8136&lon=144.9631&appid=df584a0437488bfbfafc54efe54ddced&units=metric').json()
	my_date = date.today()
	calendar.day_name[my_date.weekday()]
	day_count = [1, 2, 3, 4, 5, 6, 7, 8]
	context = {
		'apidata' : apidata,
		'apidata_7day' : apidata_7day,
		'day_count': day_count, 
	}

	return render(request, 'html/index.html', context)

def search(request): 
	city = str(request.GET.get('city'))
	postcode = str(request.GET.get('postcode'))
	country = str(request.GET.get('country'))
	print (postcode+country)
	apilink = "https://api.openweathermap.org/data/2.5/weather?lat="+postcode+"&lon="+country+"&appid=df584a0437488bfbfafc54efe54ddced&units=metric"
	apidata_7day = 'https://api.openweathermap.org/data/2.5/onecall?lat='+postcode+'&lon='+country+'&appid=df584a0437488bfbfafc54efe54ddced&units=metric'
	api_7day = requests.get(apidata_7day).json()
	apidata = requests.get(apilink).json()
	data = {'apidata' : apidata, 'api_7day' : api_7day}
	return JsonResponse(data)