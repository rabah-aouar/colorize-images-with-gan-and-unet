from .views import grayscale_image
from django.urls import path, re_path


urlpatterns = [
    path('colorize',grayscale_image),
]
