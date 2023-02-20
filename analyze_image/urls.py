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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name = "upload_image"),
    path('detail/<int:number>', views.image_detail, name = "image_detail"),
    path('detail/delete/<int:number>', views.delete_image, name="remove_image"),
    path('detail/update_size/<int:number>/', views.update_size, name="update_size"),
    path('detail/update_color/<int:number>/', views.update_color, name="update_color"),
    path('detail/remove_tag/<int:number><str:tag_name>/', views.remove_tag, name="update_tag"),
    path('detail/update_tag/<int:number><str:tag_name>/', views.update_image_detail, name="update_tag"),
]
