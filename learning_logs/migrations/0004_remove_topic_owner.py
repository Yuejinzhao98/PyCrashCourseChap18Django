# Generated by Django 3.1.5 on 2021-01-19 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='owner',
        ),
    ]