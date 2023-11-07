from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile, OngoingProject
from .serializers import UserProfileSerializer, UserProfileEmailSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import send_mail
import os
from django.shortcuts import render
from django.conf import settings
from django.template.loader import render_to_string



@csrf_exempt
def userInfo(request, id_or_email=None):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

        # Validate the required fields (first_name, last_name, and email)
        required_fields = ['first_name', 'last_name', 'email']
        for field in required_fields:
            if field not in data or not data[field]:
                return JsonResponse({"error": f"Field '{field}' is required and cannot be empty."}, status=400)

        # Create a new User instance with the provided email and username
        username = data['first_name'] + data['last_name']  # Combine first_name and last_name for the username
        user = User.objects.create_user(
            email=data['email'],
            username=username,
            password=data.get('password', '')  # Optional password field
        )

        # Optionally set additional fields on the User model
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()

        # Create a new UserProfile instance and associate it with the User instance using OneToOneField
        profile = UserProfile.objects.create(
            user=user,
            approval=data.get('approval', 'pending'),  # Set default value for 'approval'
            role=data.get('role', 'user'),  # Set default value for 'role'
            organization=data.get('organization', 'none')
        )

        # Serialize the UserProfile instance to return as a response
        serializer = UserProfileSerializer(profile)  # Use your UserProfile serializer here
        return JsonResponse(serializer.data, status=201)

    elif request.method == 'GET':
        if id_or_email:
            try:
                # Try retrieving user by user ID
                if id_or_email.isdigit():
                    user_profile = UserProfile.objects.get(user_id=id_or_email)
                else:
                    # Retrieve user by email (case-insensitive search)
                    user_profile = UserProfile.objects.get(user__email__iexact=id_or_email)
            except UserProfile.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=404)

            # Serialize the UserProfile instance to return as a response
            serializer = UserProfileSerializer(user_profile)
            return JsonResponse(serializer.data)

        else:
            # Retrieve all user data
            users = UserProfile.objects.all()
            serializer = UserProfileSerializer(users, many=True)
            return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

        # Check if an ID or email is provided
        if not id_or_email:
            return JsonResponse({"error": "Please provide an ID or email for the user you want to update."}, status=400)

        # Retrieve the user based on the provided ID or email
        try:
            if id_or_email.isdigit():
                user_profile = UserProfile.objects.get(user_id=id_or_email)
            else:
                user_profile = UserProfile.objects.get(user__email__iexact=id_or_email)
        except UserProfile.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

        # Update user profile fields if provided in the request data
        if 'approval' in data:
            user_profile.approval = data['approval']
        if 'role' in data:
            user_profile.role = data['role']
        if 'organization' in data:
            user_profile.organization = data['organization']

        # Save the updated user profile
        user_profile.save()

        # Serialize the updated UserProfile instance to return as a response
        serializer = UserProfileSerializer(user_profile)
        return JsonResponse(serializer.data)

@csrf_exempt
def userInfoEmail(request, id_or_email=None):
    if request.method == 'GET':
        if id_or_email:
            try:
                # Try retrieving user by user ID
                if id_or_email.isdigit():
                    user_profile = UserProfile.objects.get(user_id=id_or_email)
                else:
                    # Retrieve user by email (case-insensitive search)
                    user_profile = UserProfile.objects.get(user__email__iexact=id_or_email)
            except UserProfile.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=404)

            # Serialize the UserProfile instance to return as a response
            serializer = UserProfileEmailSerializer(user_profile)
            return JsonResponse(serializer.data)

        else:
            # Retrieve all user data
            users = UserProfile.objects.all()
            serializer = UserProfileEmailSerializer(users, many=True)
            return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def send_email(request, user_email):
    if request.method == 'GET':
        # Get the admin emails from the .env file
        admin_emails = os.environ.get('ADMIN_EMAILS', '').split(',')

        if user_email in admin_emails:
            recipient_role = 'admin'
            print(f"{user_email} is an admin.")
        else:
            recipient_role = 'user'
            print(f"{user_email} is a user.")

        # Modify the context based on the recipient's role
        context = {
            'subject': 'User Approval - Genotype Imputation Platform',  # Replace with your subject
            'recipient_role': recipient_role,
            'user_email': user_email,  # Add the user's email to the context
        }

        # Render the email template using the Django template engine
        user_mail_html = render_to_string('user_mail.html', context)
        admin_mail_html = render_to_string('admin_mail.html', context)

        # Send email to admins
        send_mail(
            context['subject'],  # Use the subject from the context
            '',
            settings.DEFAULT_FROM_EMAIL,
            admin_emails,
            html_message=admin_mail_html,
            fail_silently=False,
        )

        # Send email to the user
        send_mail(
            context['subject'],  # Use the subject from the context
            '',
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
            html_message=user_mail_html,
            fail_silently=False,
        )

        return JsonResponse({"message": "Emails sent successfully."})

    else:
        return JsonResponse({"error": "Invalid request method."}, status=405)
      
@csrf_exempt
def allUserInfo(request):
    if request.method == 'GET':
        # Query all users from the User model
        users = User.objects.all()

        # Create an empty list to store the combined user data
        combined_user_info = []

        # Loop through each user and retrieve the associated UserProfile data
        for user in users:
            user_profile = UserProfile.objects.filter(user=user).first()

            # Create a dictionary containing both User and UserProfile data
            user_data = {
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'approval': user_profile.approval if user_profile else '',
                'role': user_profile.role if user_profile else '',
                'organization': user_profile.organization if user_profile else '',
            }

            # Append the combined user data to the list
            combined_user_info.append(user_data)

        # Return the combined user data as a JSON response
        return JsonResponse(combined_user_info, safe=False)

    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
    
@csrf_exempt
def check_ongoing_project(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        try:
            user_project = OngoingProject.objects.get(user_id=user_id)
            if user_project.project_id and user_project.expiration_date > timezone.now():
                return JsonResponse({'has_ongoing_project': True, 'project_id': user_project.project_id, 'resubmit': user_project.resubmit})
            else:
                return JsonResponse({'has_ongoing_project': False})
        except OngoingProject.DoesNotExist:
            return JsonResponse({'has_ongoing_project': False})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
    
@csrf_exempt
def add_ongoing_project(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        project_id = request.GET.get('project_id')
        resubmit = request.GET.get('resubmit')

        if not user_id or not project_id:
            return JsonResponse({'error': 'Both user_id and project_id are required.'}, status=400)

        try:
            user_project = OngoingProject.objects.get(user_id=user_id)
            user_project.project_id = project_id
            user_project.last_accessed = datetime.now()
            user_project.expiration_date = timezone.now() + timedelta(weeks=1)
            user_project.resubmit = bool(resubmit)
            user_project.save()
            return JsonResponse({'message': 'Ongoing project added successfully.'})
        except OngoingProject.DoesNotExist:
            user_project = OngoingProject(user_id=user_id, project_id=project_id)
            user_project.expiration_date = timezone.now() + timedelta(weeks=1)
            user_project.save()
            return JsonResponse({'message': 'Ongoing project added successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
    
@csrf_exempt
def delete_ongoing_project(request):
    if request.method == 'DELETE':
        user_id = request.GET.get('user_id')
        try:
            user_project = OngoingProject.objects.get(user=user_id)
            user_project.delete()
            return JsonResponse({'message': 'Ongoing project deleted successfully.'})
        except OngoingProject.DoesNotExist:
            return JsonResponse({'message': 'No ongoing project found for this user.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)