from django.shortcuts import render
from .models import Status


def index(request):
    status = Status.objects.order_by('-created_at').first()
    return render(request, 'status/index.html', {'status': status})
