from django.db import models



def track_image_path(instance):
    return instance.title


class Singer(models.Model):
    name = models.CharField(max_length=70,default=None)
    p_name = models.CharField(
        max_length=50, primary_key="true", unique=True, default=None)
    slug=models.SlugField(default=None,max_length=100)    

    class Meta:
        ordering = ['p_name']

class Tag(models.Model):
    name = models.CharField(default=None, max_length=80)
    slug=models.SlugField(max_length=200,default=None)
   
    

class Album(models.Model):
    title = models.CharField(
        max_length=80, primary_key="true", unique="true", default=None)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE,default=None,related_name="albums")
    summary = models.CharField(max_length=450, default=None,null="false")
    description = models.TextField(max_length=600, default=None)
    date = models.DateField(default=None)
    rate = models.PositiveIntegerField( default=0)
    cover = models.ImageField(upload_to="my_music_site/images", default=None)
    music = models.FileField(upload_to="my_music_site/musices", default=None)
    slug=models.SlugField(max_length=100,default=None)



class Track(models.Model):
    title = models.CharField(
        max_length=50,primary_key=True, default=None, unique=True)   
    summary = models.CharField(max_length=750, default=None,null=True)
    image = models.ImageField(upload_to="my_music_site/images", default=None)
    music = models.FileField(upload_to="my_music_site/musics", default=None)
    text = models.TextField(max_length=7000, default=None,null=True)
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, blank="true",related_name="album_track",default=None,null=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, default=None,related_name="tracks")
    rate = models.PositiveIntegerField( default=0)
    date = models.DateField(default=None)
    slug=models.SlugField(default=None,max_length=100)
    category=models.ForeignKey(Tag,default=None,on_delete=models.PROTECT ,related_name="posts")


class Music_video(models.Model):
    title = models.CharField(
        max_length=20, primary_key="true", default=None, unique=True)
    summary = models.CharField(max_length=750, default=None)
    image = models.ImageField(upload_to="my_music_site/images", default="none")
    video = models.FileField(upload_to="my_music_site/videos", default="none")
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, default="none",related_name="videos")
    rate = models.FloatField(null="true", default=0)
    slug=models.SlugField(max_length=100,default=None)


class Comments(models.Model):
    post = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='comments')
    نام = models.CharField(max_length=200)
    ایمیل=models.EmailField(default=None)
    متن= models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    
 

class album_Comments(models.Model):
    post= models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_comments')
    نام = models.CharField(max_length=200)
    ایمیل=models.EmailField(default=None)
    متن= models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
  
class music_video_Comments(models.Model):
    post = models.ForeignKey(Music_video, on_delete=models.CASCADE, related_name='clip_comments')
    نام = models.CharField(max_length=200)
    ایمیل=models.EmailField(default=None)
    متن= models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
   
