# Generated by Django 4.2.3 on 2023-07-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlkapi', '0014_alter_orderinfo_bin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitem',
            name='Status',
            field=models.CharField(blank=True, db_column='Status', default='Pending', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='OrderNumber',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='OrderNumber'),
        ),
    ]
