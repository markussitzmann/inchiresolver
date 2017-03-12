# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntryPoint',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=4096)),
                ('description', models.TextField(blank=True, max_length=32768, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inchi',
            fields=[
                ('uid', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('version', models.IntegerField(db_column='version_id')),
                ('is_standard', models.BooleanField(db_column='is_standard')),
                ('block1', models.CharField(db_column='block1', max_length=14)),
                ('block2', models.CharField(db_column='block2', max_length=10)),
                ('block3', models.CharField(db_column='block3', max_length=1)),
                ('key', models.CharField(blank=True, db_column='key', max_length=27, null=True)),
                ('string', models.CharField(blank=True, max_length=32768, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=32768, null=True, unique=True)),
                ('abbreviation', models.CharField(blank=True, max_length=32, null=True)),
                ('url', models.URLField(blank=True, max_length=4096, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resolver.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=32768, null=True)),
                ('group', models.CharField(blank=True, max_length=32768, null=True)),
                ('contact', models.CharField(blank=True, max_length=32768, null=True)),
                ('url', models.URLField(blank=True, max_length=4096, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resolver.Organization')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resolver.Publisher')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='inchi',
            unique_together=set([('block1', 'block2', 'block3', 'version')]),
        ),
        migrations.AddField(
            model_name='entrypoint',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resolver.Publisher'),
        ),
        migrations.AlterUniqueTogether(
            name='publisher',
            unique_together=set([('parent', 'organization', 'name', 'group', 'contact')]),
        ),
        migrations.AlterUniqueTogether(
            name='entrypoint',
            unique_together=set([('publisher', 'url')]),
        ),
    ]
