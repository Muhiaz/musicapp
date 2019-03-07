from django.conf.urls import url
from . import views

urlpatterns =[
#music
url(r'^$', views.ListView.as_view(), name='home'),
# music/registration_form.html
url(r'^register/$',views.UserFormView.as_view(),name='user-login'),
url(r'^videos/$',views.MusicListView.as_view(), name='videos'),
url(r'^song/$',views.SongCreate.as_view(), name='song'),
#music/<album_id>
url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#music/<album_id/favorite
# url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favorite,name='favorite')
#music/album/add
url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-create'),
#music/album/2 -the update view
url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),
url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumDelete.as_view(),name='album-delete'),
 ]
 