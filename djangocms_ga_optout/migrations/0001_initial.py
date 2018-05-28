# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='GAOptout',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_ga_optout_gaoptout', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('link_label', models.CharField(help_text='Link text displayed to user', max_length=511, verbose_name='Link label')),
                ('success_text', models.CharField(help_text='Text displayed when link is clicked. If empty, no alert will be shown.', max_length=511, verbose_name='Success text', blank=True)),
            ],
            options={
                'verbose_name': 'GA Optout',
                'verbose_name_plural': 'GA Optouts',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
