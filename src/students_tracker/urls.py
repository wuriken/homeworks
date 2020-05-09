"""students_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from groups.views import create_group

from students.views import create_student, generate_student, generate_students

from students_tracker.views import index

from teachers.views import create_teacher
from teachers.views import get_teachers


urlpatterns = [
    path('admin/', admin.site.urls),

    path('generate-student/', generate_student),
    path('generate-students/', generate_students),
    path('get-teachers/', get_teachers),

    path('', index),
    path('students/create', create_student),
    path('groups/create', create_group),
    path('teachers/create', create_teacher),
]
