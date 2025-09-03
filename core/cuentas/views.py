from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.urls import reverse

# Create your views here.
def registro(request):
    form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form':form})

@require_POST
def api_registro(request):
    form = CustomUserCreationForm(request.POST, request.FILES)
    if form.is_valid():
        user = form.save()
        return JsonResponse({
            'ok': True,
            'url' : reverse('cuentas:login')
        })
    else:
        return JsonResponse({
            'ok': False,
            'errors' : form.errors
        }, status = 400)



def loginView(request):
    return render(request, 'login.html')

@require_POST
def login_api(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user is None:
            return JsonResponse({
                'ok': False, 
                'errors': "Credenciales Invalidas"
            })
        
        return JsonResponse({
            'ok': True,
            "respuesta": "Inicio de sesion correcto",
            'url' : reverse('Home:Home')
        })
        
        
    except Exception as e:
        return JsonResponse({
            'ok': False,
            'errors': str(e)
        }, status=400)
        




def logoutView(request):
    logout(request)
    return redirect('cuentas:login')