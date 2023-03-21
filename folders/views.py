from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from .models import *
from .forms import *

########################################### create new folder, new note and delete
def new_folder(request, title):
    # user profile
    profile = request.user.profile
    
    # date and time settings
    date = datetime.datetime.now()
    month = date.strftime("%B")
    year = date.strftime("%Y")
    day = date.strftime("%d")
    hour = date.strftime("%I")
    min = date.strftime("%M")
    am_pm = date.strftime("%p")
    time = f"{day} {month} {year} at {hour}:{min}{am_pm}"

    # get all created folders
    all_folders = profile.foldername_set.all()

    # get folder with title
    folder_title = FolderName.objects.get(title=title)
    
    # use the getNoteCount func from models.py file
    # to update num of notes for a specific folder name / title
    folder_title.getNotesCount

    # get all notes for a specific folder
    notes = folder_title.note_set.all()


    # form for creating new folders
    folder_form = FolderNameCreationForm()

    # form for creating new notes
    form = NoteCreationForm()

    # request method to handle form CRUD functionality 
    # for creating notes and folders
    if request.method == 'POST':
        # delete a specific folder with all associated notes
        if 'delete' in request.POST:
            folder_title.delete()

            # delete folder message
            messages.error(request, f'[ {folder_title} ] folder deleted successful')
            return redirect('all-notes')
        
        # create new notes for a specific folder
        if 'create_note' in request.POST:
            form = NoteCreationForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.name = folder_title
                note.save()
                folder_title.getNotesCount

                # create note message
                messages.success(request, f'[ {note.title} ] note created successful')
                return redirect(request.path_info)
            
        # create new folder
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
    context = {'all_folders': all_folders, 'folder_title': folder_title, 'folder_form': folder_form, 'form': form, 'time': time, 'notes': notes}
    return render(request, 'folders/new-folder.html', context)

########################################## update and delete folder note
def update_and_delete_folderNote(request, pk):
    # user profile
    profile = request.user.profile

    # date and time settings
    date = datetime.datetime.now()
    month = date.strftime("%B")
    year = date.strftime("%Y")
    day = date.strftime("%d")
    hour = date.strftime("%I")
    min = date.strftime("%M")
    am_pm = date.strftime("%p")
    time = f"{day} {month} {year} at {hour}:{min}{am_pm}"

    # get all created folders
    all_folders = profile.foldername_set.all()

    # form for creating new folders
    folder_form = FolderNameCreationForm()
    
    # get a specific note
    note = Note.objects.get(id=pk)

    # note creation form
    form = NoteCreationForm(instance=note)
    if request.method == 'POST':
        # check if the delete button was clicked, 
        # if YES delete the specific note
        if 'delete' in request.POST:
            note.delete()

            # delete note message
            messages.error(request, f'[ {note.title} ] note deleted successful')
            # change the 8000 to your port number 
            # if you're not using port 8000
            return redirect(f'http://127.0.0.1:8000/folder/{note.name}/')
        
        # if the delete button was not clicked, 
        # get specific folder note instace and update it
        form = NoteCreationForm(request.POST, instance=note)
        if form.is_valid():
            form.save()

            # create update note message
            messages.success(request, f'[ {note.title} ] updated successful')
            # change the 8000 to your port number 
            # if you're not using port 8000
            return redirect(f'http://127.0.0.1:8000/folder/{note.name}/')
        
        # create new folder
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
    context = {'form': form, 'time': time, 'note': note, 'all_folders': all_folders, 'folder_form': folder_form}
    return render(request, 'folders/update-folder-note.html', context)