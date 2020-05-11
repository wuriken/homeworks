from django.urls import path

from groups import views

app_name = 'groups'

urlpatterns = [
    path('create/', views.create_group, name='create'),
    path('edit/<int:pk>/', views.edit_group, name='edit'),
    path('delete/<int:pk>/', views.delete_group, name='delete'),
    path('list/', views.groups, name='list'),
]
