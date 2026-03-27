from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_data",views.get_data, name="get_data"),
    path("redirect", views.redirect, name="redirect"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
