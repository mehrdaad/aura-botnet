# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-03 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_type', models.CharField(max_length=15)),
                ('hash_sum', models.CharField(max_length=200)),
                ('group', models.IntegerField(default=0)),
                ('operating_sys', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=20)),
                ('ip_addr', models.CharField(max_length=16)),
                ('geolocation', models.CharField(max_length=100)),
                ('last_contact', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Bot_Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_completed', models.DateTimeField(default=django.utils.timezone.now)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convey.Bot')),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmd_txt', models.TextField(default='')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='start_time')),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='end_time')),
                ('group_assigned', models.IntegerField(blank=True, default=-2, null=True)),
                ('hash_assigned', models.CharField(blank=True, max_length=200, null=True)),
                ('oneshot', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='bot_command',
            name='cmd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='convey.Command'),
        ),
        migrations.AddField(
            model_name='bot',
            name='completed_cmds',
            field=models.ManyToManyField(through='convey.Bot_Command', to='convey.Command'),
        ),
    ]
