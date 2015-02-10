# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Facility'
        db.create_table(u'infrastructure_facility', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')(null=True)),
            ('abbreviation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['general.District'], null=True, blank=True)),
        ))
        db.send_create_signal('infrastructure', ['Facility'])

        # Adding model 'Designation'
        db.create_table(u'infrastructure_designation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('infrastructure', ['Designation'])

        # Adding model 'Employee'
        db.create_table(u'infrastructure_employee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')(null=True)),
            ('last_name', self.gf('django.db.models.fields.TextField')(null=True)),
            ('title', self.gf('django.db.models.fields.TextField')(null=True)),
            ('identification_number', self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True)),
            ('designation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['infrastructure.Designation'], null=True, blank=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['infrastructure.Facility'], null=True, blank=True)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True)),
        ))
        db.send_create_signal('infrastructure', ['Employee'])


    def backwards(self, orm):
        # Deleting model 'Facility'
        db.delete_table(u'infrastructure_facility')

        # Deleting model 'Designation'
        db.delete_table(u'infrastructure_designation')

        # Deleting model 'Employee'
        db.delete_table(u'infrastructure_employee')


    models = {
        'general.country': {
            'Meta': {'object_name': 'Country'},
            'abbreviation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'general.district': {
            'Meta': {'object_name': 'District'},
            'abbreviation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['general.Country']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'infrastructure.designation': {
            'Meta': {'object_name': 'Designation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'infrastructure.employee': {
            'Meta': {'object_name': 'Employee'},
            'contact_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'designation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['infrastructure.Designation']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['infrastructure.Facility']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identification_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'infrastructure.facility': {
            'Meta': {'object_name': 'Facility'},
            'abbreviation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['general.District']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['infrastructure']