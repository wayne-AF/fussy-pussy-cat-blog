from .models import Comment, Profile, Post
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


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'content')
        # 'featured_image'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


    # title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    # # one-to-many r'ship from the user
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    # updated_on = models.DateTimeField(auto_now=True)
    # content = RichTextField(blank=True, null=True)
    # # content = models.TextField()
    # featured_image = models.ImageField(null=True, blank=True, upload_to='images/')
    # excerpt = models.TextField(blank=True)
    # created_on = models.DateTimeField(auto_now=True)
    # status = models.IntegerField(choices=STATUS, default=1)
    # likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)



# class EditForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'slug', 'content', 'featured_image')