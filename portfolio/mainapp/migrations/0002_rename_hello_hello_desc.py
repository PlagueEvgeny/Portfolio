# Generated by Django 4.0.3 on 2022-03-31 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hello',
            old_name='hello',
            new_name='desc',
        ),
    ]
