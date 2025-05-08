from django.urls import path
from .views import index, submit_total

urlpatterns = [
    path('index/', index, name='index-page'),
    path('submit-total/', submit_total, name='submit-total'),
]
