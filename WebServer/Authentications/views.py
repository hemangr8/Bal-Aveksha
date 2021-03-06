from django import template
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from  Counsellee.models import CounselleeDetails
from Counsellor.models import CounsellorDetails
from Authentications.forms import RegistrationForm


def homepageView(request):
    '''
    URL: '/'
    Opens bal-aveksha homepage
    '''
    return render(request, 'homepage/index.html')


@api_view(['GET'])
@permission_classes([AllowAny])
def setprofileView(request, username):
    '''
    URL: '/profile'
    Opens Set User Profile Page if user is logged in
             otherwise responds with HTTP_401_UNAUTHORIZED
    '''
    return render(request, 'profile/setprofile.html')


def signupView(request):
    '''
    URL: '/signup'
    Opens Sign Up Page
    '''
    return render(request, 'signup/signup.html')


def Index(request):
    return render(request, 'Home/index.html', {'user': request.user})


#
# class RegisterUser(View):
#     form_class = RegistrationForm
#     template_name = 'registration/register.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False)
#
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             email = form.cleaned_data['email']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             user.set_password(password)
#             user.save()
#
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return render(request, 'Profile/profileRedirect.html', {'username': username})
#                 else:
#                     return render(request, self.template_name, {'form': form, 'message': 'Could not activate'})
#             else:
#                 return render(request, self.template_name, {'form': form, 'message': 'Could not login'})
#
#         else:
#             message = 'Something Went wrong please fill in correct details'
#             form = self.form_class(None)
#             return render(request, self.template_name, {'form': form, 'message': message})


# @csrf_protect
# def register_success(request):
#     return render(request, 'Authentications/Index.html')







#
# class UserList(APIView):
#     """
#     List all albums, or create a new album.
#     """
#     # def get(self, request, format=None):
#     #     user = User.objects.all()
#     #     serializer = UserSerializer(user, many=True)
#     #     return Response(serializer.data)
#
#     def get(self, request, format = None):
#         serializer=UserSerializer(data=request.data)
#  #        serializer = UserSerializer(data=request.data)
#   #       if serializer.is_valid():
#              #serializer.save()
#         user = authenticate(username="arjun1234", password="123456")
#         if user is not None:
#             return Response(user, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)



@csrf_exempt
def checkUser(request):
    username = request.POST['username']
    u_id = User.objects.get(username=username).id
    # loggedinUser = User.objects.get(username=username)
    # counsellorList = tuple(CounsellorDetails.objects.all())
    if CounsellorDetails.objects.filter(username_id=u_id).exists():
        role = 'Counsellor'
        # HttpResponseRedirect(username+'/counsellordashboard/')
        return HttpResponse(role)
        # return render(request, 'dashboard/counsellordashboard.html')
    else:
        # render_to_response(template_name='dashboard/counselleedashboard.html')
        # return render(request, 'dashboard/counselleedashboard.html')
        role = 'Counsellee'
        # HttpResponseRedirect(reverse(username + '/counselleedashboard/'))
        return HttpResponse(role)
        # except:
        #return HttpResponse(request, status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, JSONWebTokenAuthentication])
def counsellorDashboardView(request, username):
    '''
    URL: '/'
    Opens counsellor homepage
    '''
    return render(request, template_name='dashboard/counsellordashboard.html')


@csrf_exempt
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication,JSONWebTokenAuthentication])
def counselleeDashboardView(request, username):
    '''
    URL: '/'
    Opens counsellee homepage
    '''

    return render(request, template_name='dashboard/counselleedashboard.html')
