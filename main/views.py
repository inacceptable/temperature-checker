
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
def index(request):
	apidata = requests.get('https://api.openweathermap.org/data/2.5/weather?q=melbourne,3000,australia&appid=df584a0437488bfbfafc54efe54ddced&units=metric').json()
	context = {
		'apidata' : apidata,
	}
	return render(request, 'html/index.html', context)

def search(request): 
	city = str(request.GET.get('city'))
	postcode = str(request.GET.get('postcode'))
	country = str(request.GET.get('country'))
	apilink = "https://api.openweathermap.org/data/2.5/weather?q="+city+","+postcode+","+country+"&appid=df584a0437488bfbfafc54efe54ddced&units=metric"
	apidata = requests.get(apilink).json()
	data = {'apidata' : apidata}
	return JsonResponse(data)