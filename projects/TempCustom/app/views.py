from django.shortcuts import render
from django.utils import timezone


def humanize(request):
    now = timezone.now()
    context = {
        'apnumber': [1, 2, 4, 5, 6, 7, 8, 9, 10],
        'intcomma': [4500, 4500.2, 45000, 450000, 4500000],
        'intword': [1000000, 1200000, 1200000000],
        'naturalday': [(now - timezone.timedelta(days=1)).date,
                       now.date,
                       (now + timezone.timedelta(days=1)).date],
        'naturaltime': [now - timezone.timedelta(minutes=30),
                        now - timezone.timedelta(minutes=15),
                        now],
        'ordinal': [1, 2, 3, 4, 5]
    }
    return render(request, 'human.html', context)


