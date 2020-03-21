from django.shortcuts import render, HttpResponse
from .tasks import task_1, task_2


def test_celery_task(request):
    task_1.delay()
    task_2.delay()
    return HttpResponse('<h1>Task working</h1>')
