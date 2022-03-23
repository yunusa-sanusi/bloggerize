from django.contrib import admin
from posts.models import Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published',
                    'last_modified', 'views',)


admin.site.register(Tag)
