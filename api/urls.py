from django.urls import path

from api import views

urlpatterns = [
    path("demo_1/", views.demo_1.as_view()),
    path("demo_2/", views.demo_2.as_view()),
]
