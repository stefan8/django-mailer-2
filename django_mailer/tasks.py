#-*- coding: utf-8 -*-
from django.core import management
from datetime import timedelta
from celery.task import PeriodicTask


class SendMail(PeriodicTask):
    run_every = timedelta(minutes=1)

    def run(*args, **kwargs):
        management.call_command('send_mail')


class SendDeferredMail(PeriodicTask):
    run_every = timedelta(minutes=5)

    def run(*args, **kwargs):
        management.call_command('retry_deferred')
