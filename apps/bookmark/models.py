from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    TitleSlugDescriptionModel,
    ActivatorModel,
)


class Bookmark(TimeStampedModel, ActivatorModel):
    title = models.CharField(blank=True, max_length=255)
    link = models.CharField(max_length=255, unique=True)
    tags = models.ManyToManyField('bookmark.Tag', null=True, blank=True)
    owner = models.ForeignKey('auth.User', null=True, blank=True)
    
    def __unicode__(self):
        return self.title + ' ' + self.link

class Tag(TitleSlugDescriptionModel):
    
    def __unicode__(self):
        return self.title

