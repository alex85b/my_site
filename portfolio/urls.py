from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view()),
    path("<slug:slug>", views.ProjectDetailsVeiw.as_view(), name="project-details")
]