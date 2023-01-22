from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
# from django.core.mail import send_mail
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Post, Profile
from .forms import CommentForm, EditProfileForm, CreatePostForm, UpdatePostForm, ChangePasswordForm
# UpdateProfileForm


class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('')

def password_success(request):
    return render(request, 'password_success.html', {})


class PostList(generic.ListView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )



class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


# # @login_required



def contact(request):
    return render(request, 'contact.html', {})


class AddPostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



class UserEditView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'edit_account.html'
    success_url = reverse_lazy('home')

    # def edit_profile_form(request):
    #     if request.method == 'POST':
    #         # user_form = UpdateUserForm(request.POST, instance=request.user)
    #         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

    #         if profile_form.is_valid():
    #             # user_form.save()
    #             profile_form.save()
    #             messages.success(request, 'Your profile has been updated successfully!')
    #             return render(request, 'profile.html', {'profile_form': profile_form})
    #         else:
    #             for error in profile_form.errors:
    #                 print(profile_form)
    #                 print("Error: ", error)
    #     else:
    #         # user_form = UpdateUserForm(instance=request.user)
    #         profile_form = UpdateProfileForm(instance=request.user.profile)

    #     return render(request, 'edit_profile.html', {'profile_form': profile_form})
    
    def get_object(self):
        return self.request.user