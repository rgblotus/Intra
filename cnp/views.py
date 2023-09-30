from django.shortcuts import render
from django.conf import settings
import os, json

from cnp.models import Indent, Indentor
from core.views import load_fixture


# Create your views here.
def cnp(request):
    # Read JSON data from a file or from an API
    #filepath = os.path.join(settings.BASE_DIR, 'Assets/static/app/doc/cnp.json')
    #with open(filepath) as json_file:
    #    json_data = json.load(json_file)

    context = {'indentors': Indentor.objects.all(), 'indents': Indent.objects.all(), 'fixture':load_fixture('cnp', 'cnp.json')}
    return render(request, 'cnp.html', context)


def indent_detail(request):
    context = {'cnp': Indentor.objects.all(), 'indents': Indent.objects.all()}
    return render(request, 'indent.html', context)

def team_detail(request):
    context = {'cnp': Indentor.objects.all(), 'indents': Indent.objects.all()}
    return render(request, 'team.html', context)