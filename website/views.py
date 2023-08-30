from cgitb import html
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from website.models import enquiry_table
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


from .models import enquiry_table
from .serializers import enquiry_tableSerializer
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

def index(request):
    return render(request, 'index.html')

def aboutproject(request):
    return render(request, 'aboutproject.html')

def problem_statement(request):
    return render(request, 'problem-statement.html')

def scope_project(request):
    return render(request, 'scope-of-the-project.html')

def reg_form_house_wife(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        enquiry = enquiry_table(name=name, email=email, phone=phone, address=address)
        enquiry.save()
        messages.success(request, 'Enquiry Sent Successfully...')


    return render(request, 'Reg-Form-House-Wife.html')

def reg_form_company(request):
    return render(request, 'Reg-Form-Company.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            request.session['username_id'] = username
            return redirect('dashboard/')
        else:
            # display 'invalid login' error message
            messages.error(request, 'In-correct username or password!..')    
        
    return render(request, 'login.html')


@login_required(login_url='login')
def dashboard(request):
    info = enquiry_table.objects.all()
    # enquiry_table is table name which we create in models.py
    
    data = {'information':info}
    print('You are logged in, Hi',request.session.get('username_id'))
    return render(request, 'dashboard/index.html',data)


def logout_user(request):
    logout(request)
    return redirect('/')


def enquiry_info(request):
    info = enquiry_table.objects.all()
    # enquiry_table is table name which we create in models.py
    
    data = {'information':info}
    return render(request, 'dashboard/tables.html', data)

def delete_record(request, id):
    if request.method=='POST':
        data = enquiry_table.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/info/')

def edit_record(request, id):
    info = enquiry_table.objects.filter(pk=id)
    data = {'information':info}
    return render(request, 'dashboard/editrecord.html', data)

def update_record(request, id):
    info = enquiry_table.objects.get(pk=id)
    
    info.name = request.POST.get('name')
    info.email = request.POST.get('email')
    info.phone = request.POST.get('phone')
    info.address = request.POST.get('address')
    info.save()
    
    return HttpResponseRedirect('/info/')


# def student_data(request):
#     data = enquiry_table.objects.all()
#     # Creating Model instance
    
#     serializer = enquiry_tableSerializer(data, many=True)
#     # Converting model instance to serialized data

#     # json_data = JSONRenderer().render(serializer.data)
#         # Converting serialized data into JSON String

#     # return HttpResponse(json_data, content_type='application/json')
#         # and we need to specify content type here.
#     return JsonResponse(serializer.data, safe=False)
#     # In order to allow non-dict objects to be serialized set the safe parameter to False.


class student_data(APIView):
    def get(self, request, format=None):
        data = enquiry_table.objects.all()
        serializer = enquiry_tableSerializer(data, many=True)
        return Response(serializer.data)

# Above class for browsable APIView data showing to user



    