from django.urls import path
from . import views

urlpatterns = [
    path('ipo/', views.ipo_page, name='ipo_page'),
]
