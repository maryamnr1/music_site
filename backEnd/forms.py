from django import forms
from .models import Comments,album_Comments,music_video_Comments



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('نام','ایمیل','متن')
        widgets = {
            'نام': forms.TextInput(attrs={'class': 'user_name', 'placeholder': 'نام خود را وارد نمایید'}),
            'ایمیل': forms.EmailInput(attrs={'class': 'email', 'placeholder': 'ایمیل خود را وارد نمایید'}),
            'متن': forms.Textarea(attrs={'class': 'comment_body', 'placeholder': 'نظرتان را بنویسید...'})

           }
        
class CommentForm_album(forms.ModelForm):

    class Meta:
        model = album_Comments
        fields = ('نام','ایمیل','متن')
        widgets = {
            'نام': forms.TextInput(attrs={'class': 'user_name', 'placeholder': 'نام خود را وارد نمایید'}),
            'ایمیل': forms.EmailInput(attrs={'class': 'email', 'placeholder': 'ایمیل خود را وارد نمایید'}),
            'متن': forms.Textarea(attrs={'class': 'comment_body', 'placeholder': 'نظرتان را بنویسید...'})

           }

class CommentForm_video(forms.ModelForm):

    class Meta:
        model = music_video_Comments
        fields = ('نام','ایمیل','متن')
        widgets = {
            'نام': forms.TextInput(attrs={'class': 'user_name', 'placeholder': 'نام خود را وارد نمایید'}),
            'ایمیل': forms.EmailInput(attrs={'class': 'email', 'placeholder': 'ایمیل خود را وارد نمایید'}),
            'متن': forms.Textarea(attrs={'class': 'comment_body', 'placeholder': 'نظرتان را بنویسید...'})

           }