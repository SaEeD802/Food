from django.urls import path
from .views import show, PostDetail


urlpatterns = [
    path('', show, name='home'),
    path('<int:pk>/', PostDetail.as_view(), name='detail'),
]