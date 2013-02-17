from django.contrib import admin
from bookmark.models import Bookmark, Tag

class BookmarkAdmin(admin.ModelAdmin):
    exclude = ('activate_date', 'deactivate_date')
    list_display = ('link', 'title', 'status')
    list_filter = ('status', 'tags', 'owner')
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.save()
    
admin.site.register(Bookmark, BookmarkAdmin)

admin.site.register(Tag)
