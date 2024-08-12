# user - monit
# pass - 1


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    #     if username!='' and password != '':
    #         response = HttpResponse("Login successful")
    #         response.set_cookie('username', username)
    #         return response
    #     else:
    #         return HttpResponse("Invalid login")
    # return render(request, 'myapp/login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponse("Login successful")
            response.set_cookie('username', username)
            return response
        else:
            return HttpResponse("Invalid login")
    return render(request, 'myapp/login.html')

def logout_view(request):
    logout(request)
    response = HttpResponse("Logged out")
    response.delete_cookie('username')
    return HttpResponse("Logged out")
    
