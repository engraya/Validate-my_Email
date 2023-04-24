from django.urls import path
from . import views 


urlpatterns = [
    path("validatePage/", views.validatePage, name="validatePage"),
    path("", views.homePage, name="homePage"),
]
