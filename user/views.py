from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from folders.models import *
from folders.forms import *
from .forms import *

########################################## home page views
def homePage(request):
    return render(request, 'user/home.html')

################################ register User views
def registerPage(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,  'user account created successful')
            login(request, user)
            return redirect('get-started')

    context = {'form': form}
    return render(request, 'user/sign-up.html', context)

################################ login views
def loginPage(request):
    # 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,  'User not found')


        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            # user login success message
            messages.success(request,  'user login successful')
            return redirect('get-started')
        else:
            messages.error(request,  'Username or Password is incorrect')

    return render(request, 'user/login.html')

################################ logout views
def logoutPage(request):
    logout(request)
    return redirect('login')

#################################  user profle views
@login_required(login_url='login')
def userProfile(request):
    # user profile
    profile = request.user.profile

    # user profile form INSTANCE
    form = UserProfileForm(instance=profile)

    # get all created folders
    all_folders = profile.foldername_set.all()

    # form for creating new folders
    folder_form = FolderNameCreationForm()
    if request.method == 'POST':
        if 'create_folder' in request.POST:
            folder_form = FolderNameCreationForm(request.POST)
            if folder_form.is_valid():
                folder = folder_form.save(commit=False)
                folder.account_owner = profile
                folder.save()

                # create new folder message
                messages.success(request, f'[ {all_folders[0]} ] folder created successful')
                # change the 8000 to your port number 
                # if you're not using port 8000
                return redirect(f'http://127.0.0.1:8000/folder/{all_folders[0]}/')
        
        # user profile form
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            # create new folder message
            messages.success(request,  'profile updated successful')
            # change the 8000 to your port number 
            # if you're not using port 8000
        else:
            profile.delete()
            # create new folder message
            messages.success(request, 'account delete successful')
            return redirect('home')

    context = {'all_folders': all_folders, 'folder_form': folder_form, 'form': form}
    return render(request, 'user/user-profile.html', context)





