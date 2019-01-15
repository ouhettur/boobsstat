# Generated by Django 2.1.5 on 2019-01-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlembicVersion',
            fields=[
                ('version_num', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'alembic_version',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('sum_rating', models.IntegerField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('count_rating', models.IntegerField(blank=True, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('media_type', models.TextField(blank=True, null=True)),
                ('telegram_file_id', models.TextField(blank=True, null=True)),
                ('reports_count', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'img',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inlinequery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField()),
                ('query', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'InlineQuery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('rated_at', models.DateTimeField(blank=True, null=True)),
                ('reported_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'show',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('upload_rating', models.IntegerField(blank=True, null=True)),
                ('view_rating', models.IntegerField(blank=True, null=True)),
                ('chat_name', models.TextField(blank=True, null=True)),
                ('first_name', models.TextField(blank=True, null=True)),
                ('last_name', models.TextField(blank=True, null=True)),
                ('login', models.TextField(blank=True, null=True)),
                ('language_code', models.TextField(blank=True, null=True)),
                ('role', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]