from . import views
from .views import AddPostView, UpdatePostView, DeletePostView, UserEditView, PasswordsChangeView
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    # because using class-based views, must use as_view() after PostList so it will render the class as a view
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('edit_account/<int:user_id>/', views.UserEditView.as_view(), name='edit_account'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='update_post'),
    path('delete/<slug:slug>/', DeletePostView.as_view(), name='delete_post'),
    path('edit_account/password/', PasswordsChangeView.as_view(template_name='change-password.html')),
    path('password/password_success/', views.password_success, name='password_success'),

    

]