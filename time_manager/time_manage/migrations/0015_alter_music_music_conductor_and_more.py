# Generated by Django 4.0.3 on 2022-04-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_manage', '0014_alter_music_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='music_conductor',
            field=models.CharField(blank=True, default='해당 없음', max_length=100),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_label_id',
            field=models.CharField(blank=True, default='해당 없음', max_length=50),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_orchestra',
            field=models.CharField(blank=True, default='해당 없음', max_length=200),
        ),
        migrations.AlterField(
            model_name='timeinfo',
            name='time_manager',
            field=models.CharField(max_length=100),
        ),
    ]
