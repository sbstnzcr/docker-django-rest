from django.http.response import HttpResponse
from django.urls import path

app_name = 'api'


def view(request):
    return HttpResponse()

urlpatterns = [
    path('status/', view, name='status'),
]
