from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('create-activity-log/', create_user_activity_log, name='create-activity-log'),
    path('get-activity-log/', get_user_activity_logs, name='get-activity-logs'),
    path('events/<platform>/<pipeline_id>/<runId>/<userId>/<projectId>/None/null', events.as_view()),
    # Add more URL patterns as needed
]
