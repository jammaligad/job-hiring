from django.urls import path, include
from . import views
from users import views as user_views

app_name = 'job_platform'

urlpatterns = [
    path('', user_views.index, name="index"),
    path('home/', views.home, name="home"),
    path('create_job/',views.create_job, name="create_job"),
]
