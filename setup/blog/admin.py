from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "content")
    list_filter = ("author", "created_at", "updated_at")

admin.site.register(Post, PostAdmin)