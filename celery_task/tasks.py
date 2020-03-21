# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from time import sleep


@shared_task
def task_1():
    print('Start task 1')
    sleep(2)
    print('End task 1')
    return


@shared_task
def task_2():
    print('Start task 2')
    sleep(3)
    print('End task 2')
    return
