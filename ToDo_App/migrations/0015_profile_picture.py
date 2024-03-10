# Generated by Django 4.2.11 on 2024-03-06 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_App', '0014_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]