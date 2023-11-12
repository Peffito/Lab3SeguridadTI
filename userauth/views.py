# In views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from userauth.packages import SQLI
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        correctUser="admin"
        correctPass="MskD#3nVJ}izBZ@'gq'Q;H_0zfD)I+S'FOQz"
        username = request.POST['username']
        password = request.POST['password']
        query =  "SELECT * FROM Users WHERE username =" + username + "AND password = " + password #Simular Query
        if username is not None:	
        	if ((correctUser in username) and SQLI.sql_injection_check(query)): #detectar SQL Injection en el username	
        		return redirect('success_page')  # Redirecciona exitosamente
        	if (username == correctUser and password == correctPass):
	               return redirect('success_page')   	
	       	if (username not in correctUser): #Verifica el usuario
        		return HttpResponse("Usuario Incorrecto")
        	if (password not in correctPass): #Verifica la contraseña
        		return HttpResponse("Contraseña Incorrecta")
        	else:
	       	        return HttpResponse("El inicio de sesión ha fracasado.")	
        else:
            # Handle invalid login
            return HttpResponse("El inicio de sesión ha fracasado.")


    return render(request, 'userauth/login.html')
    
def success_page(request):
    return render(request,'userauth/success_page.html')
