# coding: utf-8
import datetime

import github3
from django.utils import timezone
from django_cron import CronJobBase, Schedule

from pythonstars_app.models import DataPoint


class GetDataCronjob(CronJobBase):
    RUN_EVERY_MINS = 360  # 6 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'pythonstars_app.cronjobs.GetDataCronjob'

    def do(self):
        author, reponame = 'python', 'cpython'
        repository = github3.repository('python', 'cpython')
        stars = repository.stargazers
        DataPoint.objects.create(
            author=author,
            repository=reponame,
            stars=stars,
        )


class AggregateCronjob(CronJobBase):
    RUN_EVERY_MINS = 60  # 1 hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'pythonstars_app.cronjobs.AggregateCronjob'

    def do(self):
        one_month_ago = timezone.now() - datetime.timedelta(days=30)

        datapoints = DataPoint.objects.filter(
            recorded_at__year=one_month_ago.year,
            recorded_at__month=one_month_ago.month,
            recorded_at__day=one_month_ago.day,
        )

        try:
            latest = datapoints.latest('recorded_at')
        except DataPoint.DoesNotExist:
            pass
        else:
            datapoints.exclude(pk=latest.pk).delete()
