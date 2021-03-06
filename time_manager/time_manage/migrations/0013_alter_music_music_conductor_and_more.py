# Generated by Django 4.0.3 on 2022-04-12 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_manage', '0012_alter_music_options_alter_player_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='music_conductor',
            field=models.CharField(blank=True, default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_label_id',
            field=models.CharField(blank=True, default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_orchestra',
            field=models.CharField(blank=True, default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_source',
            field=models.CharField(default='CD', max_length=100),
        ),
    ]
