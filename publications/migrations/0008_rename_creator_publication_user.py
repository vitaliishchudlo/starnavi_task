# Generated by Django 3.2.5 on 2021-07-29 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0007_alter_like_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='creator',
            new_name='user',
        ),
    ]
