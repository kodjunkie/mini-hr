from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
# noinspection PyPep8Naming
from django.contrib.auth import (
    authenticate,
    logout as logoutUser,
    login as loginUser
)
from django.urls import reverse
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from .decorators import guest_only
from django.core.files.storage import default_storage
from .forms import UserForm


@guest_only
def index(request):
    """
    The login page
    :param request:
    :return:
    """
    return render(request, 'users/auth/login.html')


@guest_only
def login(request):
    """
    Process the login credentials
    :param request:
    :return:
    """
    if request.method == 'POST' and request.is_ajax():
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            loginUser(request, user)
            return JsonResponse({
                'msg': 'Login successful.',
                'error': False
            })
        else:
            return JsonResponse({
                'msg': 'Invalid username or password, try again.',
                'error': True
            })
    else:
        return HttpResponseForbidden('Not allowed.')


def logout(request):
    """
    Log out the auth user
    :param request:
    :return:
    """
    logoutUser(request)
    messages.success(request, 'Logged out successfully.')
    return redirect(reverse('users:index'))


@login_required
def edit(request):
    form = UserForm(instance=request.user)
    return render(request, 'users/edit.html', {'form': form})


@login_required
def update(request):
    """
    Process the post request
    :param request:
    :return:
    """
    if request.method == 'POST' and request.is_ajax():
        form = UserForm(request.POST, request.FILES, instance=request.user)
        old_avatar = request.user.avatar.path if request.user.avatar and request.FILES.get(
            'avatar') is not None else None
        if form.is_valid():
            form.save()
            if old_avatar is not None:
                default_storage.delete(old_avatar)

            return JsonResponse({
                'msg': 'Profile successfully updated.',
                'error': False
            })
        else:
            return JsonResponse({
                'msg': 'Your input didn\'t pass validation, check and try again.',
                'error': True
            })
    else:
        return HttpResponseForbidden('Not allowed.')


@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')
