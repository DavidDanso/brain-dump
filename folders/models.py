from django.db import models
from user.models import Profile
import uuid

# folder model    
class FolderName(models.Model):
    account_owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    number_of_notes = models.IntegerField(default=0, null=True, blank=True)
    updated_time_stamp = models.DateTimeField(auto_now=True)
    created_time_stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    # func to calculate the number of notes in a folder
    @property
    def getNotesCount(self):
        notes = self.note_set.all()
        total_notes = notes.count()
        self.number_of_notes = total_notes
        self.save()

    # change all submmited or created folder names to lowercase
    def save(self, *args, **kwargs):
        self.title = self.title.lower() # Capitalize the title field
        super(FolderName, self).save(*args, **kwargs)
    
    # display new folders first
    class Meta:
        ordering = ['-updated_time_stamp']

    # display folders with titles in the database
    def __str__(self):
        return self.title

# Create your models here.    
class Note(models.Model):
    name = models.ForeignKey(FolderName, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=100000, null=True)
    updated_time_stamp = models.DateTimeField(auto_now=True)
    created_time_stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    # display new folders first
    class Meta:
        ordering = ['-updated_time_stamp']

    # display folders with titles with only 15 charaters in the database
    def __str__(self):
        return self.title[:15] + "..."