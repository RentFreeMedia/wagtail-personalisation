# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('wagtail_personalisation', '0012_remove_personalisablepagemetadata_is_segmented'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='count',
            field=models.PositiveSmallIntegerField(default=0, help_text='If this number is set for a static segment users will be added to the set until the number is reached. After this no more users will be added.'),
        ),
        migrations.AddField(
            model_name='segment',
            name='sessions',
            field=models.ManyToManyField(to='sessions.Session'),
        ),
        migrations.AddField(
            model_name='segment',
            name='type',
            field=models.CharField(choices=[('dynamic', 'Dynamic'), ('static', 'Static')], default='dynamic', help_text='\n            </br></br><strong>Dynamic:</strong> Users in this segment will change\n            as more or less meet the rules specified in the segment.\n            </br><strong>Static:</strong> If the segment contains only static\n            compatible rules the segment will contain the members that pass\n            those rules when the segment is created. Mixed static segments or\n            those containing entirely non static compatible rules will be\n            populated using the count variable.\n        ', max_length=20),
        ),
    ]