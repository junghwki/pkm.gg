# Generated by Django 3.2.7 on 2021-09-22 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0035_auto_20210922_0436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='type2',
            new_name='type',
        ),
    ]
