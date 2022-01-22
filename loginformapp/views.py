from django.shortcuts import render
from .models import LoginData


def login_view(request):
    if request.method == 'POST':
        LoginData(
        email = request.POST['email'],
        password = request.POST['password']
        ).save()

        return render(request, 'login.html')
    
    else:

        return render(request, 'login.html')
