import json 
import os 
from pathlib import Path
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomPasswordResetForm, CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm

# Create your views here.
def home(request):
    if request.method == "POST":
        registrationForm = CustomUserCreationForm(request.POST)
        loginForm = CustomAuthenticationForm(request, data=request.POST)
        #Login
        if 'login_submit' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if  user is not None:
                login(request, user)
                return JsonResponse({"success": True})
            else:
                errors = loginForm.errors.as_json()
                return JsonResponse({"success": False, "errors": errors})
        #Register   
        elif 'register_submit' in request.POST:
            if registrationForm.is_valid():
                password = registrationForm.cleaned_data['password1']
                mobilenumber = registrationForm.cleaned_data['mobile_number']
                if str(mobilenumber).isdigit():
                    # Registration logic
                    confirm_password = registrationForm.cleaned_data['password2']
                    if password == confirm_password:
                        user = registrationForm.save()
                        login(request, user)
                        return JsonResponse({"success": True})
                else:
                    error_message = "Please enter phone number in digit only."
                    return JsonResponse({"success": False, "error_message": error_message})
            else:
                errors = registrationForm.errors.as_json()
                return JsonResponse({"success": False, "errors": errors})
    else:
        registrationForm = CustomUserCreationForm()
        loginForm = CustomAuthenticationForm()
        resetPasswordForm = CustomPasswordResetForm()
    

    return render(request, 'index.html', {'registrationForm': registrationForm, 'loginForm': loginForm, 'resetPasswordForm' : resetPasswordForm, 'fixture':load_fixture('core', 'hazira.json')})

#Logout
def logoutuser(request):
    logout(request)
    return redirect('home')

def test(request):
    return render(request, 'test.html', {})

def load_fixture(app, fixture_name):
    fixture_path = Path(os.path.join(settings.BASE_DIR, app, "fixtures", fixture_name))
    with open(fixture_path) as f:
        if fixture_path.suffix == ".json":
            fixture = json.load(f)
        else:
            fixture = f.read()
        return fixture
    