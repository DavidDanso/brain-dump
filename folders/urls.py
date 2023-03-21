from django.urls import path
from . import views

urlpatterns = [
    path('<str:title>/', views.new_folder, name='notes'),
    path('update-note/<str:pk>/', views.update_and_delete_folderNote, name='update-note'),
]