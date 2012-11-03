# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmployeeType'
        db.create_table('shifts_employeetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('shifts', ['EmployeeType'])

        # Adding model 'Employee'
        db.create_table('shifts_employee', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shifts.EmployeeType'])),
        ))
        db.send_create_signal('shifts', ['Employee'])

        # Adding model 'Shift'
        db.create_table('shifts_shift', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('employee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['shifts.Employee'])),
        ))
        db.send_create_signal('shifts', ['Shift'])


    def backwards(self, orm):
        # Deleting model 'EmployeeType'
        db.delete_table('shifts_employeetype')

        # Deleting model 'Employee'
        db.delete_table('shifts_employee')

        # Deleting model 'Shift'
        db.delete_table('shifts_shift')


    models = {
        'shifts.employee': {
            'Meta': {'object_name': 'Employee'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shifts.EmployeeType']"})
        },
        'shifts.employeetype': {
            'Meta': {'object_name': 'EmployeeType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'shifts.shift': {
            'Meta': {'object_name': 'Shift'},
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shifts.Employee']"}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['shifts']