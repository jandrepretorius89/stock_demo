# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StockItem'
        db.create_table(u'stock_stockitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('trade_name', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('abreviation', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('class_name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
            ('cas_number', self.gf('django.db.models.fields.CharField')(max_length=25, unique=True, null=True)),
            ('va_class', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
        ))
        db.send_create_signal('stock', ['StockItem'])

        # Adding model 'StockLevel'
        db.create_table(u'stock_stocklevel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('stock_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stock.StockItem'], null=True, blank=True)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['infrastructure.Facility'], null=True, blank=True)),
            ('minimum_level', self.gf('django.db.models.fields.IntegerField')()),
            ('current_level', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('stock', ['StockLevel'])

        # Adding unique constraint on 'StockLevel', fields ['stock_item', 'facility']
        db.create_unique(u'stock_stocklevel', ['stock_item_id', 'facility_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'StockLevel', fields ['stock_item', 'facility']
        db.delete_unique(u'stock_stocklevel', ['stock_item_id', 'facility_id'])

        # Deleting model 'StockItem'
        db.delete_table(u'stock_stockitem')

        # Deleting model 'StockLevel'
        db.delete_table(u'stock_stocklevel')


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
        'infrastructure.facility': {
            'Meta': {'object_name': 'Facility'},
            'abbreviation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['general.District']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'stock.stockitem': {
            'Meta': {'object_name': 'StockItem'},
            'abreviation': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'cas_number': ('django.db.models.fields.CharField', [], {'max_length': '25', 'unique': 'True', 'null': 'True'}),
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'trade_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'va_class': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'})
        },
        'stock.stocklevel': {
            'Meta': {'unique_together': "(('stock_item', 'facility'),)", 'object_name': 'StockLevel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_level': ('django.db.models.fields.IntegerField', [], {}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['infrastructure.Facility']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimum_level': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'stock_item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock.StockItem']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stock']