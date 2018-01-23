# coding: utf-8
import github3
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
