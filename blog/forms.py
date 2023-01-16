from .models import Comment, Profile
from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class UpdateUserForm(forms.ModelForm):
    username = forms.Charfield(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    cat_idol = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    likes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dislikes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['profile_pic', 'cat_idol', 'likes', 'dislikes', 'bio']