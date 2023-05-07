from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserSignupForm
from django.contrib.auth import login, logout
from .models import Profile


def signin(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main:index')
    return render(request, 'signin.html', {'form': form})


def signup(request):
    form = UserSignupForm()

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main:index')
    return render(request, 'signup.html', {"form": form})


def signout(request):
    logout(request)
    return redirect(request, 'main:index')


def new_profile(request):
    # 로그인 하지 않았다면 프로필 눌러도 홈으로 이동
    if request.user.is_anonymous:
        return redirect('main:index')
    # 로그인 했다면 해당 유저의 프로필 보기
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'newProfile.html', {"profile":profile})
    # 프로필이 원래 존재했으면 created=False

def create_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        profile.nickname = request.POST.get('nickname')
        profile.image = request.FILES.get('image')
        profile.save()
        return redirect('user:new_profile')
    return render(request, "newProfile.html", {'profile':profile})