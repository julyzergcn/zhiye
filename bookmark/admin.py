from django.contrib import admin
from bookmark.models import Bookmark, Tag

class BookmarkAdmin(admin.ModelAdmin):
    exclude = ('activate_date', 'deactivate_date', 'owner')
    list_display = ('title', 'link_url', 'tags_list', 'status')
    list_filter = ('status', 'tags')
    list_editable = ('status', )
    
    def link_url(self, obj):
        return '<a href="%s" target="_blank">%s</a>' % (obj.link, obj.link)
    link_url.allow_tags = True
    
    def tags_list(self, obj):
        return ', '.join([t.title for t in obj.tags.all()])
    
    def save_model(self, request, obj, form, change):
        obj.title = obj.title or 'nt'
        obj.owner = request.user
        obj.save()
    
admin.site.register(Bookmark, BookmarkAdmin)

admin.site.register(Tag)
