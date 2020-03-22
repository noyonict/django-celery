from django.shortcuts import HttpResponse
from django_celery.celery import task_1, task_2


def test_celery_task(request):
    """
    Testing task_1 and task_2 is working.
    :param request:
    :return: a sample web response!
    """
    task_1.delay()
    task_2.delay()
    return HttpResponse('<h1>Task_1 and Task_2 is working. Both are handled by Celery.</h1>')
