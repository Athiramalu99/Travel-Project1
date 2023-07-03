from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')

    return render(request, "login.html")


# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         if User.objects.filter(username=username).exists():
#             messages.info(request,"user taken")
#             return redirect("register")
#         else:
#             user = User.objects.create_user(username=username, password=password)
#             user.save();
#             print("User Created")
#             return redirect('login')
#     return render(request, "register.html")


def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if full_name != '':
            if email != '':
                if password == confirm_password:
                    if password != '':
                        if User.objects.filter(username=email).exists():
                            messages.info(request, "Email Already Taken")
                            return redirect('register')
                        else:
                            if len(password) < 8:
                                messages.info(request, "Password must have 8 characters")
                            else:
                                user = User.objects.create_user(username=email, password=password, email=email, first_name=full_name)
                                user.save()
                                return redirect('login')
                    else:
                        messages.info(request, "Password is Empty")
                else:
                    messages.info(request, "Password doesn't match")
            else:
                messages.info(request, "Please enter your email.id")
        else:
            messages.info(request, "Please enter your Full name")

    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
