from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('world_cups/', views.worldcups_index, name='index'),
    path('world_cups/<int:cup_id>', views.worldcups_details, name='detail'),
    path('world_cups/create/',
         views.CupCreate.as_view(),
         name='world_cups_create'),
    path('world_cups/<int:pk>/update/',
         views.CupUpdate.as_view(),
         name='world_cups_update'),
    path('world_cups/<int:pk>/delete/',
         views.CupDelete.as_view(),
         name='world_cups_delete'),
    path('world_cups/<int:cup_id>/add_fan/', views.add_fan, name='add_fan'),
]