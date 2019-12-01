from django.urls import path
from . import views

app_name = 'calendario'
urlpatterns = [
    path('add_evento/', views.add_event, name='add_evento'),
    path('calendar/', views.calendar, name='calendar'),
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),

]
