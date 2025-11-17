from django.http import HttpResponse

def index(request):
    return HttpResponse("Lotto Basic Project Running")
