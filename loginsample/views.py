from django.http import HttpResponse


def home(request):
    return HttpResponse(f'Welcome to Login')


