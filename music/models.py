from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
	album_tittle = models.CharField(max_length=120)
	artist = models.CharField(max_length=120)
	genre = models.CharField(max_length=120)
	album_logo = models.FileField()
	
	# inorder for a user to create an album and it is saved in the database
	def get_absolute_url(self):
		return reverse('music:detail',kwargs={'pk':self.pk})
	def __str__(self):
		return self.album_tittle + '-' + self.artist
class Song(models.Model):
	song = models.FileField(max_length=120, default=False)
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_tittle = models.CharField(max_length=200)
	is_favorite = models.BooleanField(default = False)
	def __str__(self):
		return self.song_tittle
class Music(models.Model):
	image = models.FileField()
	artist = models.CharField(max_length=120)
	song_tittle =models.CharField(max_length=120)
	def __str__(self):
		return self.song_tittle
		