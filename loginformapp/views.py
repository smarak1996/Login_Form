from django.shortcuts import render
from .models import LoginData
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
    
        email = request.POST['email']
        password = request.POST['password']

        if LoginData.objects.filter(email = email, password = password).exists():
            
            return render(request, 'success.html')

        else:

            messages.warning(request, 'Invalid Email Address!!!')
            return render(request, 'login.html')
    
    else:

        return render(request, 'login.html')

def sign_up_view(request):
    if request.method == 'POST':
        LoginData(
            email = request.POST['email'],
            password = request.POST['password']
        ).save()

        return render(request, 'sign_up.html')

    else:
        return render(request, 'sign_up.html')






























