# Generated by Django 4.2.3 on 2023-07-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopifyhook', '0004_hook_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hook',
            name='source',
            field=models.CharField(choices=[(0, 'Shopify'), (1, 'ShipStation')], max_length=20, verbose_name='Source'),
        ),
    ]