# Generated by Django 4.2.3 on 2023-07-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlkapi', '0011_alter_lineitem_customer_alter_lineitem_customeremail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='TrackingNumber',
            field=models.CharField(blank=True, db_column='TrackingNumber', max_length=500, null=True),
        ),
    ]
