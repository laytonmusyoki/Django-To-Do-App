# Generated by Django 4.2.1 on 2023-06-06 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_create_choices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='create',
            old_name='choices',
            new_name='STATUS',
        ),
    ]