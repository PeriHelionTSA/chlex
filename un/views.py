from django.shortcuts import render

from common.models import Lem


def index(request):
    qs = Lem.objects.all()
    qs = qs.order_by('pinyin')
    return render(request, 'un/index.html', {'lemmata': qs})

def about(request):
    return render(request, 'un/about.html')

def contact(request):
    return render(request, 'un/contact.html')

def r_graph(request, graph):
    from common.models import Meaning

    #qs = Meaning.objects.filter(graphs=graph)
    qs = Lem.objects.filter(graphs=graph)
    return render(request, 'resource/graph.html', {'lemmata': qs})
