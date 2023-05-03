from django.shortcuts import render
from services.models import Service
from clients.models import Client

# Create your views here.

def index(request):
    services = Service.objects.all()
    clients = Client.objects.all()
    context = {
        'services': services,
        'clients': clients,
    }
    return render(request, 'index.html', context)