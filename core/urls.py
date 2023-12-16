from django.urls import path

from . import views

urlpatterns = [
    path("", views.sign_in, name="sign_in"),
    path("home/", views.home, name="home"),
    path("students/", views.index, name="student_list"),
    path("students/<int:pk>/delete/", views.delete_entry, name="student_delete"),
    path("students/retrieve-list/", views.retrieve_list, name="retrieve_list"),
    path("students/<int:pk>/edit/", views.student_edit, name="student_edit"),
]
