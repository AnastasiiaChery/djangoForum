"""djangoForum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_publications, name="new_publications"),

    path('post/<int:number>', views.find_publication, name="new_publications"),
    path('post/delete/<int:number>', views.delete_publication, name="new_publications"),
    path('post/like/<int:number>', views.like_publication, name="new_publications"),
    path('post/like_comment/<int:number>', views.like_comment, name="new_publications"),

    path('filtered_post/<str:string>', views.get_publications_topic, name="new_publications"),

    path('filtered_post/post/<int:number>', views.find_publication, name="new_publications"),
    path('filtered_post/post/delete/<int:number>', views.find_publication, name="new_publications"),
    path('filtered_post/post/like/<int:number>', views.like_publication, name="new_publications"),
    path('filtered_post/post/like_comment/<int:number>', views.like_comment, name="new_publications"),

    path('added/', views.add_publication, name="new_page")

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']