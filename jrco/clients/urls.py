from django.urls import path, include
from .views import ClientListView

urlpatterns = [
    path('', ClientListView.as_view(), name='our-clients')

] 
