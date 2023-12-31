# Generated by Django 4.2.3 on 2023-07-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlkapi', '0002_remove_log_mylineitemid_lineitem_order_log_lineitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lineitem',
            options={'ordering': ['-OrderNumber']},
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='BinNumber',
            field=models.IntegerField(db_column='BinNumber', default=0),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='DateModified',
            field=models.DateTimeField(auto_now=True, db_column='DateModified', null=True),
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='Quantity',
            field=models.IntegerField(blank=True, db_column='Quantity', default=0, null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='ChangeDate',
            field=models.DateTimeField(auto_now_add=True, db_column='ChangeDate'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='Active',
            field=models.BooleanField(db_column='Active', default=False),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='BinNumber',
            field=models.IntegerField(db_column='BinNumber', default=0),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='LabelPrinted',
            field=models.BooleanField(db_column='LabelPrinted', default=False),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='ShipmentCost',
            field=models.FloatField(db_column='ShipmentCost', default=0.0),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='ShipmentId',
            field=models.IntegerField(db_column='ShipmentId', default=0),
        ),
    ]
