from django.conf import settings
from django.template.context_processors import static
from django.urls import path
from . import views

from .views import SongView, SongDetailView

urlpatterns = [
    path('', SongView.as_view(), name='index'),
    path('product/<slug:slug>/', SongDetailView.as_view(), name='song-detail'),
    path('product/<slug:slug>/', views.SongDetailView.as_view(), name='song_detail'),
]

