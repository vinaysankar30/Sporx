from django.shortcuts import render
from .forms import UserForms


def login(request):
    return render(request, 'organization/login.html')


def login_succes(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            print("Worked")

    else:
        form = UserForms()

    return render(request, 'organization/home.html', {'form': form})
