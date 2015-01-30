# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('content', models.TextField(null=True, verbose_name='content', blank=True)),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('done', models.BooleanField(default=False, verbose_name='done')),
                ('last_mod', models.DateTimeField(auto_now=True, verbose_name='last modification')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('author', models.ForeignKey(related_name='items', verbose_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('last_mod', models.DateTimeField(auto_now=True, verbose_name='last modification')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(related_name='items', verbose_name='list', blank=True, to='todo.List', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='parent', blank=True, to='todo.Item', null=True),
            preserve_default=True,
        ),
    ]
