from django.urls import path
from .views import create_project, re_create_project, edit_project, delete_project, get_projects_by_user, update_file_path, get_project_by_id, submit_project, get_nextflows_by_user
from django.conf import settings

urlpatterns = [
    path('create_project/', create_project, name='create_project'),
    path('re_create_project/', re_create_project, name='re_create_project'),
    path('edit_project/<int:project_id>/', edit_project, name='edit_project'),
    path('delete_project/<int:project_id>/', delete_project, name='delete_project'),
    path('projects/<int:user_id>/', get_projects_by_user, name='get_projects_by_user'),
    path('projects/file/<int:project_id>/', update_file_path, name='update_file_path'),
    path('projects/getproject/<int:project_id>/', get_project_by_id, name='get_project_by_id'),
    path('projects/submitproject/<int:project_id>/', submit_project, name='submit_project'),
    path('projects/getnextflow/<int:user_id>/', get_nextflows_by_user, name='get_nextflows_by_user'),
    # Add more URL patterns as needed
]
