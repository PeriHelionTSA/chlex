from django.shortcuts import render

from common.models import Lem


def index(request):
    qs = Lem.objects.all()
    qs = qs.order_by('pinyin')
    return render(request, 'un/index.html', {'lemmata': qs})
