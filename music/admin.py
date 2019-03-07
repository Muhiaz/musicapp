from django.contrib import admin
from music.models import Album, Song,Music

# Register your models here.
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Music)