from django.shortcuts import render


def login(request):
    return render(request, 'organization/login.html')

def login_succes(request):
    return render(request, 'organization/login.html')
