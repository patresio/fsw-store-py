# Generated by Django 4.2.6 on 2023-10-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='name')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('imageUrl', models.CharField(max_length=255, verbose_name='image')),
            ],
        ),
    ]
