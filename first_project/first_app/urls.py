from django.urls import path
from . import views


app_name = 'first_app'

urlpatterns = [
    # http://localhost/first_app/hello
    path('hello', views.index, name='index'),
]
