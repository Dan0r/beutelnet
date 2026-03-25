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

""" Post searchterm """
def get_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            search_term = form.cleaned_data["search_term"]
            return render(request, "bagsearch/get_search.html", {"search_term":search_term})
    else:
        return HttpResponseNotAllowed(['POST'])

def table(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        
        if form.is_valid():
            search_term = form.cleaned_data["search_term"]
            data = VacuumBags.objects.filter(vacuum__contains=search_term)[:5]
            context = {"vacuumbags": data}
            return render(request,"bagsearch/table.html", context)

        else:
            return HttpResponseNotAllowed(['GET'])

"""When user submits name of vacuum, display the bag size"""
def answer_search_view(request):
    return HttpResponse("Testing...")
