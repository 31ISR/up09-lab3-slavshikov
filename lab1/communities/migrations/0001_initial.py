# Generated by Django 5.1.4 on 2024-12-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('free', models.BooleanField(default=True)),
            ],
        ),
    ]
