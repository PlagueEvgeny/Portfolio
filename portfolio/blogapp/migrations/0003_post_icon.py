# Generated by Django 4.0.3 on 2022-04-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icon/'),
        ),
    ]
