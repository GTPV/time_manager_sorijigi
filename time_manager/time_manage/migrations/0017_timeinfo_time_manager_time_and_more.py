# Generated by Django 4.0.4 on 2022-08-30 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_manage', '0016_alter_player_options_player_player_instrument_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeinfo',
            name='time_manager_time',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='timeinfo',
            name='time_manager',
            field=models.CharField(default='', max_length=100),
        ),
    ]
