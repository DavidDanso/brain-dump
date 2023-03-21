from django.urls import path
from . import views

urlpatterns = [
    path('get-started/', views.get_started, name='get-started'),
    path('all-notes/', views.all_notes, name='all-notes'),

    path('quick-note/', views.quick_note, name='quick-note'),
    path('quick-note/<str:pk>', views.update_quick_note, name='quick-note'),
]