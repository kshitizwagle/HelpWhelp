from sqlite3 import IntegrityError
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import User
from .models import Whelp
from .forms import SignupForm, LoginForm, WhelpsForm, AdopterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


def home(request):
    return render(request, 'home.html')


def posts(request):
    post = Whelp.objects.raw("""SELECT * FROM schoolproject_adopter
        AS A INNER JOIN schoolproject_whelp AS B ON A.username=B.user;""")
    current_user = str(request.user)
    return render(request, 'posts.html', {
        'posts': post,
        'current_user': current_user,
    })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST or None)
        adopter = AdopterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            if not User.objects.filter(username=username).exists():
                user = User.objects.create(
                    username=username,
                    password=make_password(password),
                    email=email
                )
                user.phone = phone
                user.save()
                adopter.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, 'Signed up successfully!')
                return redirect('home')
            else:
                messages.success(request, 'User already exists.')
                return render(request, 'signup.html', {
                    'username': username,
                    'email': email,
                    'phone': phone
                })
        else:
            print(form.errors)
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            messages.success(request, "There's error in entered data")
            return render(request, 'signup.html', {
                'username': username,
                'email': email,
                'phone': phone
            })
    else:
        return render(request, 'signup.html', {})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form = LoginForm(request.POST or None)
            username = request.POST['username']
            messages.success(
                request, 'Username or Password do not match. Try Again!')
            print(form.errors)
            return render(request, 'login.html', {'username': username})
    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return redirect('user_login')


def create_post(request):
    form = WhelpsForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user.username
        post.save()
        messages.success(request, "Post created successfully")
        return redirect('posts')
    else:
        messages.success(request, "Post couldn't be created. Internal Errors")
        for error in form.errors:
            print(error)
        return redirect('create_post')


def not_found(request, exception):
    return render(request, '404.html')


def create__(request):
    return render(request, 'create_post.html')


def delete_post(request, post_id):
    post = Whelp.objects.get(pk=post_id)
    post.delete()
    return redirect('posts')


def profile(request):
    username = str(request.user)
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'user': user})


def change_password(request):
    username = str(request.user)
    user = User.objects.get(username=username)
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('new_password')

    if check_password(old_password, user.password):
        user.set_password(new_password)
        user.save()
        messages.success(request, "Password changed successfully!")
        return render(request, 'profile.html')
    else:
        messages.success(
            request, "Password change unsuccessful, passwords do not match!")

    return redirect('change_password')


def change_password_page(request):
    return render(request, 'change_password.html')
