# Generated by Django 3.2.7 on 2021-09-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0052_rename_contents_news_url'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='pokemon',
            index=models.Index(fields=['name_text'], name='pokemon_pok_name_te_ffa9e6_idx'),
        ),
    ]
