from django.urls import path, include
from . import views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.home, name="home"),
    path('jobs/', views.jobs, name="jobs"),
    path('jobs/createjob/', views.createjob, name="createjob"),
    path('jobs/<int:job_id>/', views.detailjob, name="detailjob"),
    path('jobs/<int:job_id>/update/', views.updatejob, name="updatejob"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
