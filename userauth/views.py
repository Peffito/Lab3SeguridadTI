# In views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from userauth.packages import SQLI
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        #user = authenticate(request, username=username, password=password)
        query =  "SELECT * FROM users WHERE username =" + username + "AND password = " + password
        if username is not None:
        	if (("Christoph Molnar" in username) and SQLI.sql_injection_check(query)):
        		#login(request, username)
        		redirect('success_page')  # Redirect to a success page
        else:
            # Handle invalid login
            return HttpResponse("El inicio de sesiòn ha fracasado.")


    return render(request, 'userauth/login.html')
    
def success_page(request):
    return render(request,'userauth/success_page.html')
