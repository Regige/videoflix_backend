# Generated by Django 4.2.15 on 2024-08-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
