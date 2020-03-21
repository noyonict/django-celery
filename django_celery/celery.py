from __future__ import absolute_import, unicode_literals
import os
from time import sleep
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task
def test(arg):
    print(arg)


@app.task
def task_1():
    print('Start task 1')
    sleep(2)
    print('End task 1')
    return 'Complete Task 1'


@app.task
def task_2():
    print('Start task 2')
    sleep(3)
    print('End task 2')
    return 'Complete Task 2'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls task_1 every 60 seconds.
    sender.add_periodic_task(60.0, task_1.s(), name='run every 60 seconds')

    # Calls task_2 every 1 seconds.
    sender.add_periodic_task(1.0, task_2.s(), expires=10)


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
