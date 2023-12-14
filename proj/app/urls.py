from django.urls import path
from .views import *

urlpatterns = [
    path('reg/', index, name='home'),
    path('login/', login, name='login'),
    path('data/', data, name='data'),
    path('', posts, name='posts'),
]
