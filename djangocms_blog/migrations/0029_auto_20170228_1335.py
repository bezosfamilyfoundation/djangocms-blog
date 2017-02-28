# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0028_post_featured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'blog article', 'verbose_name_plural': 'blog articles', 'ordering': ('-featured', '-date_published', '-date_created'), 'get_latest_by': 'date_published'},
        ),
    ]
