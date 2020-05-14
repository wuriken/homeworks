from django.contrib import admin
from django.urls import include, path

from students_tracker.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('groups/', include('groups.urls')),
    path('', index, name='index'),
]
