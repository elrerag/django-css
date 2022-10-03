from django.urls import path
from .views import index

app_name="persona"

urlpatterns = [
    path("", index, name="home"),
]
