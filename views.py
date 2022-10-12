from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, "home.html")


def Iris(request):
    return render(request, "iris.html")
def Irisgraphs(request):
    return render(request, "irisgraphs.html")


def Wine(request):
    return render(request, "wine.html")
def Winegraphs(request):
    return render(request, "winegraphs.html")


def Boston(request):
    return render(request, "boston.html")
def Bostongraphs(request):
    return render(request, "bostongraphs.html")


def Cancer(request):
    return render(request, "cancer.html")
def Cancergraphs(request):
    return render(request, "cancergraphs.html")

def irisBar(request):
    return render(request, "irisbar.html")
def irisScatter(request):
    return render(request, "irisscatter.html")
def irisHistogram(request):
    return render(request, "irishistogram.html")
def irisPiechart(request):
    return render(request, "irispiechart.html")
def irisHeatmap(request):
    return render(request, "irisheatmap.html")
def irisBoxplot(request):
    return render(request, "irisboxplot.html")



def bostonScatter(request):
    return render(request, "bostonscatter.html")
def bostonHistogram(request):
    return render(request, "bostonhistogram.html")
def bostonHeatmap(request):
    return render(request, "bostonheatmap.html")
def bostonBoxplot(request):
    return render(request, "bostonboxplot.html")

def wineBar(request):
    return render(request, "winebar.html")
def wineScatter(request):
    return render(request, "winescatter.html")
def wineHistogram(request):
    return render(request, "winehistogram.html")
def wineHeatmap(request):
    return render(request, "wineheatmap.html")
def wineBoxplot(request):
    return render(request, "wineboxplot.html")

def cancerBar(request):
    return render(request, "cancerbar.html")
def cancerScatter(request):
    return render(request, "cancerscatter.html")
def cancerHistogram(request):
    return render(request, "cancerhistogram.html")
def cancerHeatmap(request):
    return render(request, "cancerheatmap.html")
def cancerBoxplot(request):
    return render(request, "cancerboxplot.html")