from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('Contact/', Contact, name='Contact'),
    path('Contacto/', Contact, name='Contacto'),
    path('About/', About, name='About'),

]