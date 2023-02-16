from django.contrib import admin

from django.contrib.auth.models import User

from analyze_image.models import ImageAnalyze
from publications.models import Topics, Publication, Comment, PostLike

@admin.register(Topics)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Publication)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class GradeAdmin(admin.ModelAdmin):
    pass
@admin.register(PostLike)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(ImageAnalyze)
class GradeAdmin(admin.ModelAdmin):
    pass

