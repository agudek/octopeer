# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-14 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20160609_1928'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pullrequest',
            unique_together=set([('repository', 'pull_request_number')]),
        ),
        migrations.AlterUniqueTogether(
            name='repository',
            unique_together=set([('owner', 'name', 'platform')]),
        ),
        migrations.AlterUniqueTogether(
            name='session',
            unique_together=set([('pull_request', 'user')]),
        ),
    ]