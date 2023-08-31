"""
URL configuration for LITRevu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path

import authentication.views
import reviews_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
        name='password_change'),
    path('change_password_done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
        name='password_change_done'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('profile_photo/upload', authentication.views.upload_profile_photo, name='upload_profile_photo'),
    path('home/', reviews_app.views.home, name='home'),
    path('ticket/add/', reviews_app.views.ticket_create, name='ticket_create'),
    path('critique/create', reviews_app.views.critique_and_ticket_create, name='critique_create'),
    path('create_critique/<int:ticket_id>/', reviews_app.views.create_critique_from_ticket,
         name='create_critique_from_ticket'),
    path('user/posts/', reviews_app.views.user_posts, name='user_posts'),

    path('ticket/<int:ticket_id>/edit/', reviews_app.views.edit_ticket, name='ticket_edit'),
    path('ticket/<int:ticket_id>/delete/', reviews_app.views.delete_ticket, name='ticket_delete'),
    path('critique/<int:critique_id>/edit/', reviews_app.views.edit_critique, name='critique_edit'),
    path('critique/<int:critique_id>/delete/', reviews_app.views.delete_critique, name='critique_delete'),

    path('follow-users/', reviews_app.views.follow_users, name='follow_users'),
    path('unfollow-user/<int:user_id>/', reviews_app.views.unfollow_user, name='unfollow_user'),
    path('search-users/', reviews_app.views.search_users, name='search_users'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
