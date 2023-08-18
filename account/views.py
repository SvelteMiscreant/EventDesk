from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import Http404, JsonResponse
from event_app.models import *
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
import pytz
from datetime import datetime
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
import json
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string
from django.core.paginator import Paginator



# Create your views here.





def register_home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        conf_password = request.POST.get('conf_password', '')
        userCheck = User.objects.filter(username =username)
        # type_of_account = request.POST.get('type_of_account')
        # print(type_of_account)
        if len(username)> 20:
            messages.warning(request,"Too Long Username!!")
        elif password != conf_password:
            messages.warning(request, "Passwords Don't Match!!")
        elif userCheck:
            messages.warning(request, "Username Already Exists , Kindly Change!!")
        else:
            user_obj = User.objects.create_user(first_name = name, password = password, email = email, username=username)

            user_obj.save()
            
            # prf =Profile(prof_user= user_obj)
            # prf.save()
            prof = get_object_or_404(Profile, user = user_obj)
            prof.type_of = "HS"
            prof.save()
            login(request, user_obj)

            messages.success(request, "Account Created Successfully!!")
            return redirect("/")
    
    return render(request, 'register_home.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user_obj = authenticate( username= username, password = password)
        print(user_obj)
        if user_obj is not None:
            login(request, user_obj)
            messages.success(request, "Logged In Successfully :^) ")
            return redirect('/')
        else:
            messages.warning(request, "Invalid Credentials : ( ")
            return redirect('/account/register_home')
    return render(request, 'log_in_page.html')


def log_out(request):
    logout(request)
    return redirect("/")   


@login_required(login_url='/account/register_home')
def delete_account(request):
    user_obj = request.user
    user_obj.delete()
    return redirect('/')
