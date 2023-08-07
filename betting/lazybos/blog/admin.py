from django.contrib import admin
from .models import Post, Comment, Tag, Kategorija

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'author', 'publication_date','foto')
    search_fields = ('pavadinimas', 'turinys')
    list_filter = ('author', 'publication_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'post', 'publication_date')
    search_fields = ('content',)
    list_filter = ('author', 'publication_date')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Kategorija)