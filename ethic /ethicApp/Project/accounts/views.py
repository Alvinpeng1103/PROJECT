from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user
from .forms import CreateUserForm, LoginForm, UpdateUserForm


# Create your views here.


@unauthenticated_user
def registerPage(request):

    # Custom form model imported from forms.py
    form = CreateUserForm()

    # If user has submitted something
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        # Check if all fields are satisfied
        if form.is_valid():
            user_object = form.save()

            # Assign student group to all new users
            group = Group.objects.get(name='researcher')
            user_object.groups.add(group)

            return redirect(loginPage)

    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):

    # If user has submitted something
    if request.method == "POST":

        form = LoginForm(request.POST)

        # check if all fields are satisfied
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                if not remember_me:

                    # will close session after browser is closed
                    request.session.set_expiry(0)

                if request.user.groups.filter(name='researcher').exists():

                    return redirect('managelist')
                elif request.user.groups.filter(name='staff').exists():
                    return redirect('approvelist')
                else:
                    logout(request)
                    redirect('login')

        # if user is invalid
        form.custom_error = True
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login.html', context)


def redirect_view(request):
    # A redirect view used to redirect any page to login view
    return redirect(loginPage)


@login_required(login_url=loginPage)
@allowed_users(allowed_roles=['researcher', 'staff'])
def editUserPage(request):
    form = UpdateUserForm(instance=request.user)
    user = request.user
    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('editprofile')

    context = {'form': form, 'user': user}
    return render(request, 'edit_profile.html', context)
