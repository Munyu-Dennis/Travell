from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('http://127.0.0.1:8000/account/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('http://127.0.0.1:8000/account/register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                
        else:
          print('password not matching')
          return redirect('http://127.0.0.1:8000/account/register')

        return redirect('/')
    else:
       return render(request, 'register.html')