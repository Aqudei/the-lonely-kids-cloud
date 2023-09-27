# Generated by Django 4.2.3 on 2023-07-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopifyhook', '0006_alter_hook_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hook',
            name='source',
            field=models.CharField(choices=[('Shopify', 'Shopify'), ('ShipStation', 'ShipStation')], default='Shopify', max_length=20, verbose_name='Source'),
        ),
    ]
