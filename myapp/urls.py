from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home_page, name='homepage')
]
