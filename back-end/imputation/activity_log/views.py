from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserActivityLog
from .serializers import UserActivityLogSerializer
from django.contrib.auth.models import User 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# Create your views here.
class events(APIView):

    def get(self, request, platform, pipeline_id, runId, userId, projectId):
        return Response({})

    def post(self, request, platform, pipeline_id, runId, userId, projectId):
        data = JSONParser().parse(request)
        print(f"-with-weblog /{platform}/{pipeline_id}/{runId}/{userId}/{projectId}/None/null")
        print(data)
        return Response({})

@csrf_exempt
def create_user_activity_log(request):
    if request.method == 'POST':
        serializer = UserActivityLogSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
    
@csrf_exempt
def get_user_activity_logs(request):
    if request.method == 'GET':
        activity_logs = UserActivityLog.objects.all()
        serializer = UserActivityLogSerializer(activity_logs, many=True)

        # Include the user data in the response
        data_with_user = []
        for log in serializer.data:
            log_data = log.copy()
            user_id = log_data.pop('user')  # Remove user_id from the log data
            log_data['user'] = {
                'id': user_id,
                'username': User.objects.get(id=user_id).username  # Fetch the username from User model
            }
            data_with_user.append(log_data)

        return JsonResponse(data_with_user, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

