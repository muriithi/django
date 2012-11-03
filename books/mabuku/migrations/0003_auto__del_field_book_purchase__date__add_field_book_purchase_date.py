# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Book.purchase__date'
        db.delete_column('mabuku_book', 'purchase__date')

        # Adding field 'Book.purchase_date'
        db.add_column('mabuku_book', 'purchase_date', self.gf('django.db.models.fields.DateField')(default=''), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Book.purchase__date'
        db.add_column('mabuku_book', 'purchase__date', self.gf('django.db.models.fields.DateField')(default=''), keep_default=False)

        # Deleting field 'Book.purchase_date'
        db.delete_column('mabuku_book', 'purchase_date')


    models = {
        'mabuku.author': {
            'Meta': {'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'mabuku.book': {
            'Meta': {'ordering': "['title']", 'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mabuku.Author']", 'symmetrical': 'False'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'purchase_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['mabuku']
