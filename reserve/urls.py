from django.urls import path
from .views import reservefood



app_name = 'reserve'
urlpatterns = [
    path('', reservefood, name='reserve'),
]