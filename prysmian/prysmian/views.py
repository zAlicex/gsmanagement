from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

@login_required(login_url='/login/')
def home(request):
    # Add some debug information
    context = {
        'user': request.user,
        'is_authenticated': request.user.is_authenticated,
        'username': request.user.username if request.user.is_authenticated else 'Não logado',
        'message': 'Você está logado!' if request.user.is_authenticated else 'Você não está logado!',
    }
    return render(request, 'home.html', context)

def test_auth(request):
    """Test view to check authentication status"""
    if request.user.is_authenticated:
        return HttpResponse(f"Autenticado como: {request.user.username}")
    else:
        return HttpResponse("Não autenticado - redirecionando para login", status=401)

def custom_logout(request):
    """Logout personalizado que redireciona diretamente para login"""
    auth_logout(request)
    return redirect('login')
