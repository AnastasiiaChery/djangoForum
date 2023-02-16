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
    path('', views.get_publications, name="post_list"),

    path('post/<int:number>', views.find_publication, name="new_publications"),
    path('post/delete/<int:number>', views.delete_publication, name="post_delete"),
    path('post/like/<int:number>', views.like_publication, name="post_like"),

    path('filtered_post/<str:string>', views.get_publications_topic, name="post_filter"),

    path('filtered_post/post/<int:number>', views.find_publication, name="new_publications"),
    path('filtered_post/post/delete/<int:number>', views.find_publication, name="post_delete"),
    path('filtered_post/post/like/<int:number>', views.like_publication, name="post_like"),

    path('added/', views.add_publication, name="new_page")

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

