from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('create_post', views.create_post, name="create_post"),
    path('posts', views.posts, name="posts"),
    path('delete_post/<post_id>', views.delete_post, name="delete_post"),
    path('create__', views.create__, name="create"),
    path('profile', views.profile, name="profile"),
    path('change_password_page', views.change_password_page, name="change_password_page"),
    path('change_password', views.change_password, name="change_password")
]

handler404 = "schoolproject.views.not_found"
