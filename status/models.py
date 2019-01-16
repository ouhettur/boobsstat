from django.db import models
import datetime


class Status(models.Model):
    user_count = models.IntegerField()
    new_user_count = models.IntegerField()

    view_count = models.IntegerField()
    new_view_count = models.IntegerField()

    image_count = models.IntegerField()
    new_image_count = models.IntegerField()

    like_count = models.IntegerField()
    new_like_count = models.IntegerField()

    dislike_count = models.IntegerField()
    new_dislike_count = models.IntegerField()

    report_count = models.IntegerField()
    new_report_count = models.IntegerField()

    inline_query_count = models.IntegerField()
    new_inline_query_count = models.IntegerField()

    created_at = models.DateTimeField()

    def save_data(self):
        self.created_at = datetime.datetime.utcnow()
        self.save()

    # def __str__(self):
    #     return self.title
