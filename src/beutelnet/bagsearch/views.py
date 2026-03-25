from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotAllowed
from django.template import loader

from .models import VacuumBags
from .forms import SearchForm

# Create your views here.
""" Submit searchterm to get_search"""
def index(request):
    form = SearchForm()
    return render(request, "bagsearch/index.html", {"form":form})

def table(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        
        if form.is_valid():
            search_term = form.cleaned_data["search_term"]
            data = VacuumBags.objects.filter(vacuum__contains=search_term)[:5]
            context = {"vacuumbags": data, "form":form}
            return render(request,"bagsearch/table.html", context)

        else:
            return HttpResponseNotAllowed(['GET'])

""" Redirect to index after click on webpage-title-icon """
def redirect(request):
    form = SearchForm()
    return HttpResponseRedirect("/", {"form":form})

"""When user submits name of vacuum, display the bag size"""
def answer_search_view(request):
    return HttpResponse("Testing...")
