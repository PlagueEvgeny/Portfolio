# Generated by Django 4.0.3 on 2022-04-01 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_rename_about_about_desc_alter_about_image_facts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('desc', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='certificate/')),
                ('file', models.FileField(blank=True, upload_to='file/certificate/')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caver', models.ImageField(blank=True, upload_to='caver/')),
                ('name', models.CharField(max_length=128)),
                ('desc', models.TextField()),
                ('github', models.URLField(blank=True, max_length=128)),
                ('company', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.ImageField(blank=True, upload_to='portfolio/')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.portfolio')),
            ],
        ),
    ]
