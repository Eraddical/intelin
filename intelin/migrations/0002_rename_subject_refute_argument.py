# Generated by Django 4.0.3 on 2022-09-18 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intelin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refute',
            old_name='subject',
            new_name='argument',
        ),
    ]
