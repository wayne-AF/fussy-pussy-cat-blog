from .models import Comment, Profile, Post
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    """
    Form for user to write a comment on a post
    """
    class Meta:
        model = Comment
        fields = ('body',)


class ChangePasswordForm(PasswordChangeForm):
    """
    Form for user to update their password
    """
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class EditProfileForm(UserChangeForm):
    """
    Form for user to update their username and email
    """
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateProfileForm(forms.ModelForm):
    """
    Form for user to update their profile information
    """
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    favourite_quote = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    breed = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    likes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dislikes = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ('favourite_quote', 'breed', 'likes', 'dislikes', 'about', 'profile_pic')


class CreatePostForm(forms.ModelForm):
    """
    Form for user to create a new post
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-file'})
        }


class UpdatePostForm(forms.ModelForm):
    """
    Form for user to update and edit a post they had previously written
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'featured_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }