# Generated by Django 4.0.3 on 2022-04-10 03:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('time_manage', '0002_music_alter_timeinfo_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='_timeinfo',
            new_name='_time_info',
        ),
        migrations.AddField(
            model_name='timeinfo',
            name='_time_unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
