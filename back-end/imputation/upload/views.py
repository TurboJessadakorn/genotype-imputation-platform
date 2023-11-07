from django.http import JsonResponse
from minio import Minio
from django.views.decorators.csrf import csrf_exempt
from .models import FileUpload
from minio_storage.storage import MinioMediaStorage
import boto3
from django.conf import settings
from datetime import timedelta
from minio.error import S3Error
from django.http import FileResponse
import zipfile
from io import BytesIO
import os

minio_client = Minio(
    endpoint=settings.MINIO_STORAGE_ENDPOINT,
    access_key=settings.MINIO_STORAGE_ACCESS_KEY,
    secret_key=settings.MINIO_STORAGE_SECRET_KEY,
    secure=settings.MINIO_STORAGE_USE_HTTPS,
)

# Create your views here.
def generate_presigned_url(request):
    user_id = request.GET.get('user_id')
    project_id = request.GET.get('project_id')
    file_name = request.GET.get('file_name')

    file_path = f"{user_id}/{project_id}/input/{file_name}"

    # Set the expiration for the presigned URL (expires_in_seconds is an integer)
    expires_in_seconds = 3600
    expires = timedelta(seconds=expires_in_seconds)

    try:
        # Check if the bucket exists, if not, create it
        bucket_name = settings.MINIO_STORAGE_STATIC_BUCKET_NAME
        bucket_exists = minio_client.bucket_exists(bucket_name)
        if not bucket_exists:
            minio_client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully.")

        # Generate presigned URL
        presigned_url = minio_client.presigned_put_object(bucket_name, file_path, expires=expires)
        return JsonResponse({'presigned_url': presigned_url})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    

def list_files_in_minio(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        project_id = request.GET.get('project_id')

        if user_id and project_id:
            try:
                path_prefix = f"{user_id}/{project_id}/input/"

                # List objects in the bucket
                objects_list = []
                total_size_gb = 0

                for obj in minio_client.list_objects(settings.MINIO_STORAGE_STATIC_BUCKET_NAME, prefix=path_prefix):
                    objects_list.append([
                        obj.object_name.split('/')[-1],   # Extract the file name from the object name
                        obj.size / (1024 * 1024 * 1024)    # Convert size from bytes to gigabytes
                    ])
                    total_size_gb += obj.size / (1024 * 1024 * 1024)

                count = len(objects_list)

                return JsonResponse({'status': 'success', 'myfile': objects_list, 'size': total_size_gb, 'count': count})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@csrf_exempt
def delete_file_from_minio(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        project_id = request.POST.get('project_id')
        filename = request.POST.get('filename')  # Filename to be deleted

        if user_id and project_id and filename:
            try:

                path = f"{user_id}/{project_id}/input/{filename}"

                # Check if the file exists in MinIO
                if minio_client.bucket_exists(settings.MINIO_STORAGE_STATIC_BUCKET_NAME):
                    minio_client.remove_object(settings.MINIO_STORAGE_STATIC_BUCKET_NAME, path)

                    # Delete the corresponding entry from the database (assuming you have a model named FileUpload)
                    try:
                        file_upload_instance = FileUpload.objects.get(file_name=filename, path=path)
                        file_upload_instance.delete()
                    except FileUpload.DoesNotExist:
                        pass

                    return JsonResponse({'status': 'success'})
                else:
                    return JsonResponse({'status': 'error', 'message': 'Bucket not found'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

@csrf_exempt
def upload_file_to_minio(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        project_id = request.POST.get('project_id')
        files = request.FILES.getlist('file')

        if user_id and project_id and files:
            try:
                custom_storage = MinioMediaStorage()

                for file in files:
                    path = f"{user_id}/{project_id}/input/{file.name}"
                    custom_storage.save(path, file)
                    file_upload_instance = FileUpload(file_name=file.name, path=path, size=file.size, project_id=project_id)
                    file_upload_instance.save()

                return JsonResponse({'status': 'success'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})



def generate_presigned_download_url(request):
    user_id = request.GET.get('user_id')
    project_id = request.GET.get('project_id')

    file_path = f"{user_id}/{project_id}/output/"

    expires_in_seconds = 3600
    expires = timedelta(seconds=expires_in_seconds)

    try:
        # Check if the bucket exists
        bucket_name = settings.MINIO_STORAGE_STATIC_BUCKET_NAME
        bucket_exists = minio_client.bucket_exists(bucket_name)
        if not bucket_exists:
            minio_client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' is not exist.")
            return JsonResponse({'error': str(e)})

        # Generate presigned URL for file download
        objects = minio_client.list_objects(bucket_name, prefix=file_path, recursive=True)

        # Create a zip file in memory
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, 'a') as zip_file:
            for obj in objects:
                # Retrieve each object and add it to the zip file
                obj_data = minio_client.get_object(bucket_name, obj.object_name)
                file_name = os.path.basename(obj.object_name)
                zip_file.writestr(file_name, obj_data.read())

        zip_buffer.seek(0)
        zip_file_path = f"{file_path.rstrip('/')}.zip"
        minio_client.put_object(bucket_name, zip_file_path, zip_buffer, len(zip_buffer.getvalue()), 'application/zip')

        # Generate presigned URL for the zip file
        presigned_url = minio_client.presigned_get_object(bucket_name, zip_file_path, expires=expires, response_headers={
            'response-content-disposition': f'attachment; filename=project_{project_id}.zip'
        })

        return JsonResponse({'presigned_url': presigned_url})
    except Exception as e:
        return JsonResponse({'error': str(e)})