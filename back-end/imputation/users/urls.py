from django.urls import path
from .views import userInfo, userInfoEmail, allUserInfo, check_ongoing_project, add_ongoing_project, delete_ongoing_project, send_email
from django.conf import settings

urlpatterns = [
    path('user/', userInfo, name='userInfo'),
    path('user/<str:id_or_email>', userInfo, name='userInfo'),
    path('useremail/', userInfoEmail, name='userInfoEmail'),
    path('useremail/<str:id_or_email>', userInfoEmail, name='userInfoEmail'),
    path('send-email/<str:user_email>/', send_email, name='send_email'),
    path('alluser/', allUserInfo, name='allUserInfo'),
    path('check-ongoing-project/', check_ongoing_project, name='check_ongoing_project'),
    path('add-ongoing-project/', add_ongoing_project, name='add_ongoing_project'),
    path('delete-ongoing-project/', delete_ongoing_project, name='delete_ongoing_project'),
    # Add more URL patterns as needed
]
