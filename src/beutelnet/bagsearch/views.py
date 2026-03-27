from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse
from django.template import loader

from .models import VacuumBags
from .forms import SearchForm

# Create your views here.
""" Submit search-term to get_data"""
def index(request):
    form = SearchForm()
    return render(request, "bagsearch/index.html", {"form":form})


""" Sends back data corresponding to search-term """
def get_data(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        
        # Get search_term from the form
        if form.is_valid():
            search_term = form.cleaned_data["search_term"]
            # Query database
            queryset = VacuumBags.objects.filter(vacuum__contains=search_term)[:5]
            # Parse QuerySet using .serialize() in the model VacuumBags
            return JsonResponse([query.serialize() for query in queryset], safe=False)

        else:
            return JsonResponse({"errors": form.errors}, status=400)

# def table(request):
#     if request.method == "GET":
#         form = SearchForm(request.GET)
#
#         if form.is_valid():
#             search_term = form.cleaned_data["search_term"]
#             data = VacuumBags.objects.filter(vacuum__contains=search_term)[:5]
#             context = {"vacuumbags": data, "form":form}
#             return render(request,"bagsearch/table.html", context)
#
#         else:
#             return HttpResponseNotAllowed("Error: Submit failed.")
""" Redirect to index after click on webpage-title-icon """
def redirect(request):
    form = SearchForm()
    return HttpResponseRedirect("/", {"form":form})


def answer_search_view(request):
    return HttpResponse("Testing...")
