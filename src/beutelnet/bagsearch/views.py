from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import VacuumBags

# Create your views here.
def index(request):
    return render(request, "bagsearch/index.html")

def table(request):
    data = VacuumBags.objects.filter(vacuum__contains="None")
    context = {"vacuumbags": data}
    return render(request,"bagsearch/table.html", context)

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
