from django.contrib import admin
from .models import Post, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Profile)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Allows for use of sumernote text editor in the admin panel
    """
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('author', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Allows for approval of comments in the admin panel
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
