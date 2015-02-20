from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from micSitCeg.models import Interesados
from django.template import RequestContext
from micSitCeg.forms import InteresadosForm
from datetime import timezone
from django.core.context_processors import csrf

# Create your views here.
def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c,  content_type="text/html")