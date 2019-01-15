# Generated by Django 2.1.5 on 2019-01-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_count', models.IntegerField()),
                ('new_user_count', models.IntegerField()),
                ('view_count', models.IntegerField()),
                ('new_view_count', models.IntegerField()),
                ('image_count', models.IntegerField()),
                ('new_image_count', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('new_like_count', models.IntegerField()),
                ('dislike_count', models.IntegerField()),
                ('new_dislike_count', models.IntegerField()),
                ('report_count', models.IntegerField()),
                ('new_report_count', models.IntegerField()),
                ('inline_query_count', models.IntegerField()),
                ('new_inline_query_count', models.IntegerField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
