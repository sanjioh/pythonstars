# coding: utf-8
import datetime
from bokeh.plotting import figure
from bokeh.embed import components
from django.shortcuts import render_to_response
from django.utils import timezone

from pythonstars_app.models import DataPoint


def home(request):
    six_months_ago = timezone.now() - datetime.timedelta(days=180)

    datapoints = (
        DataPoint.objects
        .filter(recorded_at__gt=six_months_ago)
        .only('stars', 'recorded_at')
        .order_by('recorded_at')
    )
    x, y = [], []
    for datapoint in datapoints:
        x.append(datapoint.recorded_at)
        y.append(datapoint.stars)

    plot = figure(
        x_axis_type='datetime',
        plot_width=800,
        plot_height=300,
    )

    plot.line(x, y, line_width=2)
    script, div = components(plot)

    return render_to_response(
        'pythonstars_app/home.html',
        {'script': script, 'div': div},
    )
