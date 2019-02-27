from django.urls import path, include
from . import views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'job_platform'

urlpatterns = [
    path('', user_views.index, name="index"),
    path('home/', views.home, name="home"),
    path('create_job/',views.create_job, name="create_job"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
