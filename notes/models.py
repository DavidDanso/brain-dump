from django.db import models
from user.models import Profile
import uuid

# quick note model   
class QuickNote(models.Model):
    account_owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=100000, null=True)
    updated_time_stamp = models.DateTimeField(auto_now=True)
    created_time_stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    # display new notes first
    class Meta:
        ordering = ['-updated_time_stamp']
    
    # display folders with titles with only 15 charaters in the database
    def __str__(self):
        return self.title[:15] + "..."

