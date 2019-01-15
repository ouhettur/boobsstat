from informer.models import User, Img, Show, Inlinequery
from status.models import Status
import datetime


def data_saver():
    delta = datetime.timedelta(days=1)

    time = datetime.datetime.utcnow() - delta
    data = Status()
    data.user_count = User.objects.using('boobsdb').count()
    data.new_user_count = User.objects.filter(created_at__gt=time).using('boobsdb').count()

    data.view_count = Show.objects.using('boobsdb').count()
    data.new_view_count = Show.objects.filter(created_at__gt=time).using('boobsdb').count()

    data.image_count = Img.objects.using('boobsdb').count()
    data.new_image_count = Img.objects.filter(created_at__gt=time).using('boobsdb').count()

    data.like_count = Show.objects.filter(rating=1).using('boobsdb').count()
    data.new_like_count = Show.objects.filter(rating=1).filter(rated_at__gt=time).using(
        'boobsdb').count()

    data.dislike_count = Show.objects.filter(rating =-1).using('boobsdb').count()
    data.new_dislike_count = Show.objects.filter(rating = -1).filter(rated_at__gt=time).using(
        'boobsdb').count()

    data.report_count = Show.objects.filter(reported_at__isnull= False).using('boobsdb').count()
    data.new_report_count = Show.objects.filter(reported_at__isnull= False).filter(reported_at__gt=time).using(
        'boobsdb').count()

    data.inline_query_count = Inlinequery.objects.using('boobsdb').count()
    data.new_inline_query_count = Inlinequery.objects.filter(created_at__gt=time).using('boobsdb').count()

    data.save_data()