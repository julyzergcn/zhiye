# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bookmark'
        db.create_table('bookmark_bookmark', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('activate_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('deactivate_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('bookmark', ['Bookmark'])

        # Adding M2M table for field tags on 'Bookmark'
        db.create_table('bookmark_bookmark_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bookmark', models.ForeignKey(orm['bookmark.bookmark'], null=False)),
            ('tag', models.ForeignKey(orm['bookmark.tag'], null=False))
        ))
        db.create_unique('bookmark_bookmark_tags', ['bookmark_id', 'tag_id'])

        # Adding model 'Tag'
        db.create_table('bookmark_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, populate_from='title', overwrite=False)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('bookmark', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Bookmark'
        db.delete_table('bookmark_bookmark')

        # Removing M2M table for field tags on 'Bookmark'
        db.delete_table('bookmark_bookmark_tags')

        # Deleting model 'Tag'
        db.delete_table('bookmark_tag')


    models = {
        'bookmark.bookmark': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Bookmark'},
            'activate_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'deactivate_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bookmark.Tag']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'bookmark.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'title'", 'overwrite': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['bookmark']