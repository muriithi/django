# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Book'
        db.create_table('mabuku_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('edition', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('purchase__date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('mabuku', ['Book'])

        # Adding M2M table for field authors on 'Book'
        db.create_table('mabuku_book_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['mabuku.book'], null=False)),
            ('author', models.ForeignKey(orm['mabuku.author'], null=False))
        ))
        db.create_unique('mabuku_book_authors', ['book_id', 'author_id'])

        # Adding model 'Author'
        db.create_table('mabuku_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('mabuku', ['Author'])


    def backwards(self, orm):
        
        # Deleting model 'Book'
        db.delete_table('mabuku_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table('mabuku_book_authors')

        # Deleting model 'Author'
        db.delete_table('mabuku_author')


    models = {
        'mabuku.author': {
            'Meta': {'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'mabuku.book': {
            'Meta': {'ordering': "['title']", 'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mabuku.Author']", 'symmetrical': 'False'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'purchase__date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['mabuku']
