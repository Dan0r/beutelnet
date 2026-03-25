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

    # form = SearchForm()
    # return render(request, "bagsearch/search.html", {"form": form})

def table(request):
    # get userinput
    data = VacuumBags.objects.filter(vacuum__contains="City")[:5]
    context = {"vacuumbags": data}
    return render(request,"bagsearch/table.html", context)

"""When user submits name of vacuum, display the bag size"""
def answer_search_view(request):
    return HttpResponse("Testing...")
