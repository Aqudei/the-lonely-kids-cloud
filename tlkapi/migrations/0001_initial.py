# Generated by Django 4.2.3 on 2023-07-04 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('Id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('OrderNumber', models.TextField(blank=True, db_column='OrderNumber', null=True)),
                ('Sku', models.TextField(blank=True, db_column='Sku', null=True)),
                ('Name', models.TextField(blank=True, db_column='Name', null=True)),
                ('VariantId', models.BigIntegerField(blank=True, db_column='VariantId', null=True)),
                ('VariantTitle', models.TextField(blank=True, db_column='VariantTitle', null=True)),
                ('LineItemId', models.BigIntegerField(blank=True, db_column='LineItemId', null=True)),
                ('Quantity', models.IntegerField(blank=True, db_column='Quantity', null=True)),
                ('FulfillmentStatus', models.TextField(blank=True, db_column='FulfillmentStatus', null=True)),
                ('FinancialStatus', models.TextField(blank=True, db_column='FinancialStatus', null=True)),
                ('Customer', models.TextField(blank=True, db_column='Customer', null=True)),
                ('CustomerEmail', models.TextField(blank=True, db_column='CustomerEmail', null=True)),
                ('DateModified', models.DateTimeField(blank=True, db_column='DateModified', null=True)),
                ('ProductImage', models.TextField(blank=True, db_column='ProductImage', null=True)),
                ('Notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('OrderId', models.BigIntegerField(blank=True, db_column='OrderId', null=True)),
                ('PrintedQuantity', models.IntegerField(db_column='PrintedQuantity')),
                ('BinNumber', models.IntegerField(db_column='BinNumber')),
                ('Status', models.TextField(blank=True, db_column='Status', null=True)),
                ('Shipping', models.TextField(blank=True, db_column='Shipping', null=True)),
            ],
            options={
                'db_table': 'MyLineItems',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('Id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('BinNumber', models.IntegerField(db_column='BinNumber')),
                ('OrderId', models.BigIntegerField(db_column='OrderId')),
                ('Active', models.BooleanField(db_column='Active')),
                ('LabelPrinted', models.BooleanField(db_column='LabelPrinted')),
                ('LabelData', models.TextField(blank=True, db_column='LabelData', null=True)),
                ('TrackingNumber', models.TextField(blank=True, db_column='TrackingNumber', null=True)),
                ('InsuranceCost', models.FloatField(db_column='InsuranceCost')),
                ('ShipmentCost', models.FloatField(db_column='ShipmentCost')),
                ('ShipmentId', models.IntegerField(db_column='ShipmentId')),
            ],
            options={
                'db_table': 'OrderInfoes',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('Id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('ChangeDate', models.DateTimeField(db_column='ChangeDate')),
                ('ChangeStatus', models.TextField(blank=True, db_column='ChangeStatus', null=True)),
                ('MyLineItemId', models.ForeignKey(db_column='MyLineItemId', on_delete=django.db.models.deletion.DO_NOTHING, to='tlkapi.lineitem')),
            ],
            options={
                'db_table': 'Logs',
            },
        ),
    ]
