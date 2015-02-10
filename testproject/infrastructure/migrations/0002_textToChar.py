# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Designation.name'
        db.alter_column(u'infrastructure_designation', 'name', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Facility.name'
        db.alter_column(u'infrastructure_facility', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128))
        # Adding unique constraint on 'Facility', fields ['name']
        db.create_unique(u'infrastructure_facility', ['name'])


        # Changing field 'Facility.abbreviation'
        db.alter_column(u'infrastructure_facility', 'abbreviation', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Employee.last_name'
        db.alter_column(u'infrastructure_employee', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Employee.name'
        db.alter_column(u'infrastructure_employee', 'name', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Employee.title'
        db.alter_column(u'infrastructure_employee', 'title', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Removing unique constraint on 'Facility', fields ['name']
        db.delete_unique(u'infrastructure_facility', ['name'])


        # Changing field 'Designation.name'
        db.alter_column(u'infrastructure_designation', 'name', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Facility.name'
        db.alter_column(u'infrastructure_facility', 'name', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Facility.abbreviation'
        db.alter_column(u'infrastructure_facility', 'abbreviation', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Employee.last_name'
        db.alter_column(u'infrastructure_employee', 'last_name', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Employee.name'
        db.alter_column(u'infrastructure_employee', 'name', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Employee.title'
        db.alter_column(u'infrastructure_employee', 'title', self.gf('django.db.models.fields.TextField')(null=True))

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
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'})
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
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'})
        },
        'infrastructure.facility': {
            'Meta': {'object_name': 'Facility'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['general.District']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '128', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['infrastructure']