from __future__ import absolute_import, unicode_literals

from celery import shared_task

import time


@shared_task
def sum(a, b):
    time.sleep(1)
    return a + b

@shared_task
def printInChat(msg):
    print(msg)
