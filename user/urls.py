from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListUser.as_view()),
]
