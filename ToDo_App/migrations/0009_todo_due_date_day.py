# Generated by Django 4.2.11 on 2024-03-04 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_App', '0008_remove_todo_due_date_day_remove_todo_due_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='due_date_day',
            field=models.DateField(blank=True, null=True),
        ),
    ]