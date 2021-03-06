# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-27 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'event_position',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'event_type',
            },
        ),
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('merged_at', models.DateTimeField()),
                ('closed_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'pull_request',
            },
        ),
        migrations.RemoveField(
            model_name='keystrokeevent',
            name='event_ptr',
        ),
        migrations.RemoveField(
            model_name='mouseclickevent',
            name='event_ptr',
        ),
        migrations.RemoveField(
            model_name='mousehoverevent',
            name='event_ptr',
        ),
        migrations.RemoveField(
            model_name='mousemovementevent',
            name='event_ptr',
        ),
        migrations.RemoveField(
            model_name='mousescrollevent',
            name='event_ptr',
        ),
        migrations.RemoveField(
            model_name='textselectionevent',
            name='event_ptr',
        ),
        migrations.RemoveField(
            model_name='session',
            name='ended_at',
        ),
        migrations.RemoveField(
            model_name='session',
            name='started_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='session',
            name='platform',
            field=models.CharField(default='GitHub', max_length=255),
        ),
        migrations.AlterModelTable(
            name='event',
            table='event',
        ),
        migrations.DeleteModel(
            name='KeystrokeEvent',
        ),
        migrations.DeleteModel(
            name='MouseClickEvent',
        ),
        migrations.DeleteModel(
            name='MouseHoverEvent',
        ),
        migrations.DeleteModel(
            name='MouseMovementEvent',
        ),
        migrations.DeleteModel(
            name='MouseScrollEvent',
        ),
        migrations.DeleteModel(
            name='TextSelectionEvent',
        ),
        migrations.AddField(
            model_name='eventposition',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.EventType'),
        ),
        migrations.AddField(
            model_name='session',
            name='pull_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PullRequest'),
        ),
            migrations.AddField(
            model_name='event',
            name='started_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
