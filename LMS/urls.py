from django.contrib import admin
from django.urls import path
from LMS import views

urlpatterns = [
    path("", views.index, name='home'),
    path("teacher", views.teacher, name='teacher'),
    path("student", views.student, name='student'),
    path("parent", views.parent, name='parent'),
    path("Courses", views.Coursesviews, name='Courses'),
    path("Assignment/", views.Assignmentviews, name='Assignment'),
    path("Marks/", views.Marksview, name='Marks'),
    path("studentdetails/", views.studentdetailsview, name='studentdetails')
]
