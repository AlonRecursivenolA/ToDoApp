# Generated by Django 4.2.11 on 2024-03-09 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_App', '0018_todo_reminded_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, null=True)),
                ('cate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ToDo_App.todo')),
            ],
        ),
    ]
