from django.contrib import admin
from django.urls import path

from .views import get_todo_list, get_deal



urlpatterns = [
    path('', get_todo_list),
    path('<int:id>', get_deal)
]
