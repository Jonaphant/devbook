# Generated by Django 2.1.2 on 2018-10-24 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20181024_2048'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserAccount',
        ),
    ]
