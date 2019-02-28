from django.urls import path, include
from . import views
from users import views as user_views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('jobs/', views.jobs, name="jobs"),
    path('jobs/createjob/', views.createjob, name="createjob"),
]