# Generated by Django 4.1.2 on 2022-10-15 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0002_alter_event_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='id',
            new_name='eventCode',
        ),
    ]
