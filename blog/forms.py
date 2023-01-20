from .models import Comment, Profile
from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    cat_idol = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    likes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dislikes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['profile_pic', 'cat_idol', 'likes', 'dislikes', 'bio']


# class EditForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'slug', 'content', 'featured_image')