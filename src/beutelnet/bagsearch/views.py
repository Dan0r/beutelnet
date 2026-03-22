from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import VacuumBags

# Create your views here.
def index(request):
    return render(request, "bagsearch/index.html")

def table_view(request):
    return HttpResponse("Requested data will go here.")

"""When user submits name of vacuum, display the bag size"""
def answer_search_view(request):
    return HttpResponse("Testing...")

"""Return table with the first ten items loaded"""
# def bags_view(request):
#     if request.method == "GET":
#
#         bags = VacuumBags.objects.all()
#
#         return render(request, "bagsearch/index.html", {"bags": bags})
