from django.urls import path, include
from . import views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'job_platform'

urlpatterns = [
    path('home/', views.home, name="home"),
<<<<<<< HEAD
    path('create_job/',views.create_job, name="create_job"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
    path('jobs/', views.jobs, name="jobs"),
    path('jobs/createjob/', views.createjob, name="createjob"),
]
>>>>>>> d057f28c8115c1d76ca936d9ab70d4b9837a7541
