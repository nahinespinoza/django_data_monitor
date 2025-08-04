from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests
from django.conf import settings

response = requests.get(settings.API_URL)  # URL de la API
posts = response.json()  # Convertir la respuesta a JSON
# Número total de respuestas
total_responses = len(posts)
def index(request):
    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,

    }

    return render(request, 'dashboard/index.html', data)