from django.contrib import admin

# from django_site.models import Singer
# from django_site.models import Album
# from django_site.models import Track
# from django_site.models import Tag
# from django_site.models import Music_video





from django.contrib import admin
from .models import Tag,Track,Singer,Album,Music_video,Comments,album_Comments,music_video_Comments

# Register your models here.


admin.site.register(Singer)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Tag)
admin.site.register(Music_video)
admin.site.register(Comments)
admin.site.register(album_Comments)
admin.site.register(music_video_Comments)

