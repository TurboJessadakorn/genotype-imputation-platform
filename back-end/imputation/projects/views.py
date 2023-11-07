from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Project
from .serializers import ProjectSerializer
import json
import requests
from imputation.helpers import messageRun

@csrf_exempt
def create_project(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        # Exclude the specific fields from the data when input is provided
        if 'input' in data:
            data.pop('mafvalue', None)
            data.pop('genovalue', None)
            data.pop('hewvalue', None)
            data.pop('infoscore', None)

        serializer = ProjectSerializer(data=data)

        if serializer.is_valid():
            project = serializer.save()
            return JsonResponse({'project_id': project.project_id})
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
def re_create_project(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        serializer = ProjectSerializer(data=data)

        if serializer.is_valid():
            project = serializer.save()
            return JsonResponse({'project_id': project.project_id})
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
def edit_project(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return JsonResponse({'message': 'Project does not exist'}, status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)

        serializer = ProjectSerializer(project, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_project(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        return JsonResponse({'message': 'Project does not exist'}, status=404)

    if request.method == 'DELETE':
        project.delete()
        return JsonResponse({'message': 'Project deleted successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
@csrf_exempt
def get_projects_by_user(request, user_id):
    if request.method == 'GET':
        try:
            user_id = int(user_id)
        except ValueError:
            return JsonResponse({"error": "Invalid user_id. It should be an integer."}, status=400)

        # Retrieve all projects for the specified user_id
        projects = Project.objects.filter(user_id=user_id)

        # Serialize the projects data using ProjectSerializer
        serializer = ProjectSerializer(projects, many=True)

        return JsonResponse(serializer.data, safe=False)

    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def get_project_by_id(request, project_id):
    if request.method == 'GET':
        try:
            project_id = int(project_id)
        except ValueError:
            return JsonResponse({"error": "Invalid project_id. It should be an integer."}, status=400)

        try:
            # Retrieve the project by project_id
            project = Project.objects.get(project_id=project_id)

            # Serialize the project data using ProjectSerializer
            serializer = ProjectSerializer(project)

            return JsonResponse(serializer.data)

        except Project.DoesNotExist:
            return JsonResponse({"error": "Project not found"}, status=404)

    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def update_file_path(request, project_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        input_file_path = data.get('input_file_path')

        try:
            project = Project.objects.get(project_id=project_id)

            if input_file_path:
                project.input = input_file_path
                project.save()

                return JsonResponse({'status': 'success', 'message': f'Input field updated for project ID {project_id}'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Input file path is required'})

        except Project.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': f'Project with ID {project_id} does not exist'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
    

# @csrf_exempt
# def AddProjectToNextflow(request, project_id):
#     if request.method == 'POST':
#         try:
#             project = Project.objects.get(project_id=project_id)
#         except Project.DoesNotExist:
#             return JsonResponse({'error': 'Project with this project_id does not exist.'}, status=404)

#         status_value = request.POST.get('status')
#         progress_value = request.POST.get('progress')

#         try:
#             # Check if a Project for the project already exists
#             nextflow_project = Project.objects.get(project=project)
#             return JsonResponse({'error': 'Project already exists for this project.'}, status=400)
#         except Project.DoesNotExist:
#             # Create a new Project instance and set attributes
#             nextflow = Project(project=project)
#             if status_value:
#                 nextflow.status = status_value
#             if progress_value:
#                 nextflow.progress = progress_value
#             nextflow.save()
#             return JsonResponse({'message': 'Project project added successfully.'}, status=201)
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
def submit_project(request, project_id):
    if request.method == 'POST':
        try:
            project = Project.objects.get(project_id=project_id)
        except Project.DoesNotExist:
            return JsonResponse({'error': 'Project not found'}, status=404)

        nextflow_data = {
            'project_id': project.project_id,
            'disease_name': project.diseaseName,
            'buildversion': project.buildversion,
            'inputtype': project.inputtype,
            'input': project.input,
            'ref_raw': project.ref_raw,
            'mafvalue': project.mafvalue,
            'genovalue': project.genovalue,
            'hewvalue': project.hewvalue,
            'infoscore': project.infoscore,
        }

        # Remove keys with null
        nextflow_data = {key: value for key, value in nextflow_data.items() if value is not None}

        # Submit data to Nextflow by messageRun Fn
        response = messageRun(project.user_id, project_id, project.input, nextflow_data)
        
        
        if response:
            return JsonResponse({'error': response}, status=500)
        
        else:
            return JsonResponse({'message': 'Data submitted successfully'}, status=200)


@csrf_exempt
def get_nextflows_by_user(request, user_id):
    if request.method == 'GET':
        try:
            user_id = int(user_id)
        except ValueError:
            return JsonResponse({"error": "Invalid user_id. It should be an integer."}, status=400)

        projects = Project.objects.filter(user_id=user_id)
        serializer = ProjectSerializer(projects, many=True)

        return JsonResponse(serializer.data, safe=False)