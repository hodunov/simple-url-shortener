# Generated by Django 3.1.13 on 2021-07-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('times_followed', models.PositiveIntegerField(default=0)),
                ('full_url', models.URLField()),
                ('short_url', models.CharField(blank=True, max_length=15, unique=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
