# Generated by Django 4.2.3 on 2023-09-09 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_alter_variant_option1_alter_variant_option2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Backup Date')),
                ('file', models.FileField(upload_to='backup', verbose_name='File')),
            ],
            options={
                'verbose_name': 'backup',
                'verbose_name_plural': 'backups',
            },
        ),
    ]
