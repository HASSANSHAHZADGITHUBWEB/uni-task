# Generated by Django 5.1 on 2025-04-11 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_app', '0002_meetingcategory_delete_meetingschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingform',
            name='organizer_name',
        ),
        migrations.RemoveField(
            model_name='meetingform',
            name='status',
        ),
    ]
