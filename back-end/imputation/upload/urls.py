from django.urls import path
from .views import upload_file_to_minio, list_files_in_minio, delete_file_from_minio, generate_presigned_url, generate_presigned_download_url
from django.conf import settings

urlpatterns = [
    path('minio_upload/', upload_file_to_minio, name='upload_file_to_minio'),
    path('minio_list/', list_files_in_minio, name='list_files_in_minio'),
    path('minio_del/', delete_file_from_minio, name='delete_file_from_minio'),
    path('generate_presigned_url/', generate_presigned_url, name='generate_presigned_url'),
    path('generate_presigned_download_url/', generate_presigned_download_url, name='generate_presigned_download_url'),
    # Add more URL patterns as needed
]
