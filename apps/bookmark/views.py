from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django import http

from bookmark.models import Bookmark, Tag


@staff_member_required
def index(request):
    bookmarks = Bookmark.objects.active()
    tags = Tag.objects.all()
    context = {
        'bookmarks': bookmarks,
        'tags': tags,
    }
    return render(request, 'bookmark_list.html', context)

@staff_member_required
def tag_bookmarks(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    bookmarks = Bookmark.objects.active().filter(tags=tag)
    tags = Tag.objects.all().exclude(slug=slug)
    context = {
        'bookmarks': bookmarks,
        'tags': tags,
    }
    return render(request, 'bookmark_list.html', context)
    
@staff_member_required
def deactivate_bookmark(request, pk):
    Bookmark.deactivate(pk=pk)
    next = request.GET.get('next', '/')
    return http.HttpResponseRedirect(next)
