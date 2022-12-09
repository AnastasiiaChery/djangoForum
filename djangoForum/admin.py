from django.contrib import admin

from django.contrib.auth.models import User

from publications.models import Topics, Publication, Comment, PostLike, CommentLike


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
@admin.register(CommentLike)
class GradeAdmin(admin.ModelAdmin):
    pass