# Generated by Django 4.2 on 2024-11-01 08:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_category_new_region_delete_news_new_region'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='New',
            new_name='News',
        ),
    ]
