from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from .models import Song


from .models import Song, Genre

class SongView(View):
    def get(self, request):
        songs = Song.objects.all()
        genres = Genre.objects.all()
        return render(request, 'djangosong/index.html', {
            'songs_list': songs,
            'genres': genres
        })


class SongDetailView(View):
    def get(self, request, slug):
        song = get_object_or_404(Song, url=slug)
        return render(request, 'djangosong/base_generic.html', {'song': song})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        model = Song
        template_name = "djangosong/base_generic.html"
        queryset = Song.objects.all()
        return queryset.filter(slug=self.kwargs['slug'])


