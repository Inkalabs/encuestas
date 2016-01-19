from django.http import HttpResponse


def index(request):
	return HttpResponse("Hola Mundo")

def hola(request):
	return HttpResponse("Hola")