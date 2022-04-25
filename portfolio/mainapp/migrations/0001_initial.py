# Generated by Django 4.0.3 on 2022-03-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cover_hello', models.ImageField(upload_to='hello/')),
                ('hello', models.TextField()),
            ],
        ),
    ]
