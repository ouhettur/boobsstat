from django.db import models


class Inlinequery(models.Model):
    telegram_id = models.IntegerField()
    query = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InlineQuery'


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class Img(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    archived_at = models.DateTimeField(blank=True, null=True)
    sum_rating = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    count_rating = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    media_type = models.TextField(blank=True, null=True)
    telegram_file_id = models.TextField(blank=True, null=True)
    reports_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'img'


class Show(models.Model):
    img = models.ForeignKey(Img, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    rated_at = models.DateTimeField(blank=True, null=True)
    reported_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'show'


class User(models.Model):
    telegram_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    upload_rating = models.IntegerField(blank=True, null=True)
    view_rating = models.IntegerField(blank=True, null=True)
    chat_name = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    login = models.TextField(blank=True, null=True)
    language_code = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
