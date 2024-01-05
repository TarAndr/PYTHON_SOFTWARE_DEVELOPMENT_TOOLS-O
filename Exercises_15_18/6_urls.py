# urls.py

from django.urls import path
from .views import add_auto

urlpatterns = [
    path('add_auto/', add_auto, name='add_auto'),
    # Добавьте другие маршруты, если необходимо
]
