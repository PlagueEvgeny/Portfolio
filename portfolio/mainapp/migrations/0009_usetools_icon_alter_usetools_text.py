# Generated by Django 4.0.3 on 2022-04-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_usetools_tools'),
    ]

    operations = [
        migrations.AddField(
            model_name='usetools',
            name='icon',
            field=models.ImageField(blank=True, upload_to='icon/'),
        ),
        migrations.AlterField(
            model_name='usetools',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]