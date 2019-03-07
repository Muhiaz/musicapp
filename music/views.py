from django.views import generic
from .models import Album,Song,Music
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect,render
from .forms import UserForm
from django.views.generic import View

# Creating generic views
class ListView(generic.ListView):
	template_name='music/home.html'
	def get_queryset(self):
		return Album.objects.all()
class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'
class AlbumCreate(CreateView):
	model = Album
	fields =['album_tittle','artist','genre','album_logo']

class SongCreate(CreateView):
	model = Music
	fields =['image','artist','song_tittle']

class AlbumUpdate(UpdateView):
	model = Album
	fields =['album_tittle','artist','genre','album_logo']


class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:home')

class UserFormView(View):
	form_class=UserForm
	template_name='music/registration_form.html'
	# to handle the get request where the user requests the blank form.
	def get(self, request):
		form = self.form_class(None)
		return render(request, 'music/registration_form.html',{'form':form})
	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			# to create a user object based off the UserForm
			user=form.save(commit=False)
			# cleaned_data thus normalization of the data
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns user object if user credentials are correct
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('music:home')
		return render(request,'music/registration_form.html',{'form':form})
class MusicListView(generic.ListView):
	template_name= 'music/videos.html'
	def get_queryset(self):
		return Music.objects.all()
