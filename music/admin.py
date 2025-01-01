from django.contrib import admin
from unicodedata import category

from .models import Category, Singer, Genre, Song, SongShorts, RatingStar, Rating, Reviews


admin.site.register(Category)
admin.site.register(Singer)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(SongShorts)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)