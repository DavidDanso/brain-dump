from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from folders.models import *
from folders.forms import *

########################################### get started views for project
@login_required(login_url='login')
def get_started(request):    
    # user profile
    profile = request.user.profile

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
    context = {'all_folders': all_folders, 'folder_form': folder_form}
    return render(request, 'notes/get-started.html', context)

########################################### all notes views for project
@login_required(login_url='login')
def all_notes(request):
    # user profile
    profile = request.user.profile

    # logged in user
    user = request.user

    # get all created folders
    all_folders = profile.foldername_set.all()

    # date and time settings
    date = datetime.datetime.now()
    month = date.strftime("%B")
    year = date.strftime("%Y")

    # get all quick notes for logged in user and change type to a list
    quick_notes = list(profile.quicknote_set.all())

    # get all notes for logged in user and change type to a list
    notes = list(Note.objects.filter(name__account_owner__user=user))

    # concatenate both queries to display all quick note & 
    # notes under logged in user's created folders
    all_notes = notes + quick_notes
    # 
    folder_notes = []
    for note in all_notes:
        if note in notes:
            folder_notes.append(note)
    
    # get total notes created
    note_count = len(all_notes)


    # form for creating new folders
    folder_form = FolderNameCreationForm()
    # request method to handle form CRUD functionality 
    # for creating and folders
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
    context = {'all_folders': all_folders, 'month': month, 'year': year, 'note_count': note_count, 'all_notes': all_notes, 'folder_form': folder_form, 'folder_notes': folder_notes}
    return render(request, 'notes/notebooks.html', context)

########################################### quick note views for project
@login_required(login_url='login')
def quick_note(request):
    # user profile
    profile = request.user.profile

    # get all created folders
    all_folders = profile.foldername_set.all()

    # date and time settings
    date = datetime.datetime.now()
    month = date.strftime("%B")
    year = date.strftime("%Y")
    day = date.strftime("%d")
    hour = date.strftime("%I")
    min = date.strftime("%M")
    am_pm = date.strftime("%p")
    time = f"{day} {month} {year} at {hour}:{min}{am_pm}"

    # get all notes created today and previos notes
    created_today = profile.quicknote_set.filter(created_time_stamp__date=date)
    previous_note = profile.quicknote_set.exclude(created_time_stamp__date=date).order_by('-updated_time_stamp')
    
    # form to create new quick note
    form = QuickNoteCreationForm()
    # form for creating new folders
    folder_form = FolderNameCreationForm()
    # request method to handle form CRUD functionality 
    # for creating and folders
    if request.method == 'POST':
        # create new folder
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
            
        # request.POST to create new quick note
        form = QuickNoteCreationForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.account_owner = profile
            note.save()

            # create quick note message
            messages.success(request, '[ Note ] created successful')
            return redirect('quick-note')
    context = {'created_today': created_today, 'previous_note': previous_note, 'time': time, 'form': form, 'all_folders': all_folders, 'folder_form': folder_form}
    return render(request, 'notes/quick-note.html', context)

########################################## update or delete quick note
@login_required(login_url='login')
def update_quick_note(request, pk):
    # user profile
    profile = request.user.profile

    # get all created folders
    all_folders = profile.foldername_set.all()

    # get specific quick note objects
    quick_note = profile.quicknote_set.get(id=pk)
    
    # get instance of quick note
    form = QuickNoteCreationForm(instance=quick_note)
    # form for creating new folders
    folder_form = FolderNameCreationForm()
    # request method to handle form CRUD functionality 
    # for creating and folders
    if request.method == 'POST':
        if 'create_folder' in request.POST:
            folder_form = FolderNameCreationForm(request.POST)
            if folder_form.is_valid():
                folder = folder_form.save(commit=False)
                folder.account_owner = profile
                folder.save()

                # create new folder message
                messages.success(request, f'[ {all_folders[0]} ] created successful')
                # change the 8000 to your port number 
                # if you're not using port 8000
                return redirect(f'http://127.0.0.1:8000/folder/{all_folders[0]}/')
            
        # check if the delete button was clicked
        if 'delete' in request.POST:
            # delete the quick note and redirect to the quick-note page
            quick_note.delete()

            # delete quick note message
            messages.error(request, f'[ {quick_note.title} ] delete successful')
            return redirect('quick-note')
        
        # if the delete button was not clicked, 
        # get quick note instace and update the quick note
        form = QuickNoteCreationForm(request.POST, instance=quick_note)
        if form.is_valid():
            form.save()

            # update quick note message
            messages.success(request, f'[ {quick_note.title} ] updated successful')
            return redirect('quick-note')
    context = {'form': form, 'quick_note': quick_note, 'folder_form': folder_form, 'all_folders': all_folders}
    return render(request, 'notes/view-note.html', context)