from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
from app.forms import UserForm
from app.models import Session


def index(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            time = request.POST.get('time', '')
            duration = timedelta(minutes=float(time))
            session = Session(duration=duration, date=date.today(), user=user)
            session.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'app/index.html', {'navbar': 'index'})
    else:
        return render(request, 'app/index.html', {'navbar': 'index'})


@login_required
def profile(request):
    user = request.user
    if user.is_authenticated:
        user_sessions_date_first = Session.objects.filter(user=user).order_by('-date')[:5]
        user_sessions_duration_first = Session.objects.filter(user=user).order_by('-duration')[:5]
        return render(request, 'app/profile.html', {'user_sessions_date_first': user_sessions_date_first,
                                                  'user_sessions_duration_first': user_sessions_duration_first,
                                                  'navbar': 'profile'})
    else:
        return render(request, 'app/profile.html', {'navbar': 'profile'})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('User is inactive!')
        else:
            print('Invalid login details: {0}, {1}'.format(username, password))
            return HttpResponse('Invalid login details supplied.')
    else:
        return render(request, 'app/login.html', {'navbar': 'login'})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,
                  'app/register.html',
                  {'user_form': user_form,
                   'registered': registered,
                   'navbar': 'register'})