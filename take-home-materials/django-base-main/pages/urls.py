from django.urls import path

from pages import views

urlpatterns = [
    path("", views.generate_histogram, name="generate_histogram"),
]
