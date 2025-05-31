from django.contrib import admin
from .models import Member, Album, Concert, Review, MediaItem


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'video_url']
    search_fields = ['title', 'category']

admin.site.register(Review)
admin.site.register(Member)
admin.site.register(Album)
admin.site.register(Concert)
