from unicodedata import name
from django.urls import path

from . import views

app_name = 'mahasiswa'

urlpatterns = [
    path('', views.add_mahasiswa, name='add_mahasiswa'),
    path('<str:npm>', views.get_mahasiswa, name='get_mahasiswa'),
    path('delete/<str:npm>', views.delete_mahasiswa, name='delete_mahasiswa'),
    path('update/<str:npm>', views.update_mahasiswa, name='update_mahasiswa'),
    path('photos/<str:npm>', views.add_photos, name='add_photos'),
    path('photos/get/<str:npm>', views.get_photos, name='get_photos'),
]