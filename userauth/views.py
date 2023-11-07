# In views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success_page')  # Redirect to a success page
        else:
            # Handle invalid login
            variable = "Text"

    return render(request, 'userauth/login.html')
