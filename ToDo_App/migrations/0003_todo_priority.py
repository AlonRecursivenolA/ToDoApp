# Generated by Django 4.2.11 on 2024-03-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_App', '0002_remove_todo_name_todo_author_todo_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('SUN', 'Sunday'), ('MON', 'Monday'), ('sat', 'sat'), ('wed', 'wed')], max_length=10, null=True),
        ),
    ]