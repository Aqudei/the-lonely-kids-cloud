# Generated by Django 4.2.3 on 2023-07-10 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopifyhook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hook',
            name='event',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Event'),
        ),
        migrations.AlterField(
            model_name='hook',
            name='processed',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Processed'),
        ),
    ]
