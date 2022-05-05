
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django_site.models import Tag
from django_site.models import Track
from django_site.models import Singer
from django_site.models import Album
from django_site.models import Comments,album_Comments,music_video_Comments
from .forms import CommentForm, CommentForm_album,CommentForm_video
from django.db.models import Q
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import ListView
from django_site.models import Music_video
from django.views.decorators.csrf import csrf_protect 


# Create your views here.


def home(request):

    albums = Album.objects.all()
    track_list = Track.objects.all()
    music_video = Music_video.objects.all()
    singer = Singer.objects.all()
    tag = Tag.objects.all()
    paginator = Paginator(track_list, 6)
    page = request.GET.get('page')
    tracks = paginator.get_page(page)
    dict = {
        "page": page,
        "albums": albums,
        "tracks": tracks,
        "singer": singer,
        "tag": tag,
        "music_video": music_video,
    }
    return render(request, 'django_site/project.html', dict)


def music_list(request):
    track_list = Track.objects.all()
    singer = Singer.objects.all()
    tag = Tag.objects.all()
    paginator = Paginator(track_list, 6)
    page = request.GET.get('page')
    track = paginator.get_page(page)
    dict = {
        "track": track,
        "singer": singer,
        "tag": tag,

    }
    return render(request, 'musices.html', dict)


def album_list(request):
    album_list = Album.objects.all()
    singer = Singer.objects.all()
    tag = Tag.objects.all()
    paginator = Paginator(album_list, 3)
    page = request.GET.get('page')
    album = paginator.get_page(page)
    dict = {
        "album": album,
        "singer": singer,
        "tag": tag,
    }
    return render(request, 'albums.html', dict)


def clip_list(request):
    clip_list = Music_video.objects.all()
    singer = Singer.objects.all()
    tag = Tag.objects.all()
    paginator = Paginator(clip_list, 3)
    page = request.GET.get('page')
    video = paginator.get_page(page)
    dict = {
        "video": video,
        "singer": singer,
        "tag": tag,
    }
    return render(request, "video.html", dict)


def music_post(request, id):
    
    track=Track.objects.filter(slug=id)
    singer=Singer.objects.all()
    tag=Tag.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.track = track
            form.save()
            return redirect('post', id=track.slug)
    else:
        form = CommentForm()
    dict = {
        "track": track,
        "singer": singer,
        "tag": tag,
        "form":form
        
    }
    return render(request, 'post.html', dict)


def album_post(request, id):
    dict = {}
    dict['album'] = Album.objects.filter(slug=id)
    dict['track'] = Track.objects.all
    dict['singer'] = Singer.objects.all()
    dict['tag'] = Tag.objects.all()
    return render(request, "album_post.html", dict)

def music_video_post(request, id):

    dict = {}
    dict['music_video'] = Music_video.objects.filter(slug=id)
    dict['track'] = Track.objects.all
    dict['singer'] = Singer.objects.all()
    dict['tag'] = Tag.objects.all()
    return render(request, 'music_video_post.html', dict)
    
    
@csrf_protect 
def add_comment(request, id):
    post = get_object_or_404(Track, slug=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', id=post.slug)
    else:
        form = CommentForm()
    return render(request, 'new-comment.html', {'form': form,'track':post})

@csrf_protect 
def add_comment_album(request, id):
    post = get_object_or_404(Album, slug=id)

    if request.method == "POST":
        form = CommentForm_album(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('album_post', id=post.slug)
    else:
        form = CommentForm_album()
    return render(request, 'new-comment.html', {'form': form,'album':post})

@csrf_protect 
def add_comment_video(request, id):
    post = get_object_or_404(Music_video, slug=id)

    if request.method == "POST":
        form = CommentForm_video(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('video_post', id=post.slug)
    else:
        form = CommentForm_video()
    return render(request, 'new-comment.html', {'form': form,'video':post})


def searchlist(request):
    dict = {}
    search = request.GET.get('q')
    dict['track'] = Track.objects.filter(title__icontains=search)
    dict['album'] = Album.objects.filter(title__icontains=search)
    dict['video']=Music_video.objects.filter(title__icontains=search)
    dict['tag'] = Tag.objects.all()
    dict['singer'] = Singer.objects.all()
    return render(request, 'search.html', dict)


def category(request, slug):
    dict = {
        "tag": get_object_or_404(Tag, slug=slug),
        "menu": Tag.objects.all(),
        "singer": Singer.objects.all(),
        "tracks": Track.objects.all()
    }

    return render(request, 'music_menu.html', dict)


def singer_page(request, slug):
    dict = {
        "singer": get_object_or_404(Singer, slug=slug),
        "person": Singer.objects.all(),
        "tag": Tag.objects.all(),
        "tracks": Track.objects.all(),
        "albums" : Album.objects.all(),
        "videos":Music_video.objects.all()
    }
    return render(request, 'singers.html', dict)



