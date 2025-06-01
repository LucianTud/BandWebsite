from django.contrib import admin
from .models import Member, Album, Concert, Review, MediaItem
from .models import CalendarDate
from .models import UnavailableDate


@admin.register(CalendarDate)
class CalendarDateAdmin(admin.ModelAdmin):
    list_display = ('date', 'is_unavailable')
    list_filter = ('is_unavailable',)
    ordering = ('date',)

@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'video_url']
    search_fields = ['title', 'category']

admin.site.register(UnavailableDate)
admin.site.register(Review)
admin.site.register(Member)
admin.site.register(Album)
admin.site.register(Concert)
