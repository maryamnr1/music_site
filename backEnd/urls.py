"""django_music_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django_site import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django_site.views import home, music_post, album_post, searchlist,category,music_video_post,music_list,album_list,add_comment_video,add_comment_album,singer_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('<str:id>', views.music_post, name='post'),
    path('album/<str:id>', views.album_post, name='album_post'),
    path('music_video/<str:id>',views.music_video_post,name='video_post'),
    path('category/music',views.music_list,name='music'),
    path('category/album',views.album_list,name='album'),
    path('category/music_video',views.clip_list,name='music_video'),
    path('<str:id>/comment/', views.add_comment, name='add_comment'),
    path('music_video/<str:id>/music-video-comment/', views.add_comment_video, name='add_comment_video'),
    path('album/<str:id>/album-comment/', views.add_comment_album, name='add_comment_album'),
    path('singer/<slug:slug>', views.singer_page, name='singer_page'),
    path('search/', views.searchlist, name='search'),
    path('category/<slug:slug>', views.category, name='category'),
    
    
 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
