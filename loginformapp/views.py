from django.shortcuts import render
from .models import LoginData
from django.contrib import messages 


def login_view(request):
    if request.method == 'POST':
        
        email = request.POST['email'],
        password = request.POST['password']

        if LoginData.objects.filter(email = email).exists():
            messages.warning(request, 'Email already exists!!!')
            return render(request, 'login.html')

        else:

            LoginData(
                email = email,
                password = password
            ).save()
            messages.success(request, 'Login Successfull!!!')
            return render(request, 'login.html')

    
    else:

        return render(request, 'login.html')