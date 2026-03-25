from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("table",views.table, name="table"),
    path("get_search",views.get_search, name="get_search")
]
