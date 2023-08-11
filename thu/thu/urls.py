from django.http import HttpResponse
from django.contrib import admin
from django.urls import path

def home(request):
    return HttpResponse('HELLO HELLO HELLO')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
]
