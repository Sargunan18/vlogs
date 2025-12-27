from django.urls import path
from . import views

app_name="games"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<str:slug>", views.post, name="name"),
    path("old", views.old, name="old"),
    path("new", views.new, name="new"),
    path("contact", views.contect, name="contact"),
    path("about", views.about_view, name="About"),
]
