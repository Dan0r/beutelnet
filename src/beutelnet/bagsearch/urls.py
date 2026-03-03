from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bags", views.bag_view, name="bag_view")
]
