from django.urls import include, path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),
]
