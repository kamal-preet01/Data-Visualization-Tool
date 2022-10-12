"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.Home),
    path('iris/',views.Iris),
    path('wine/',views.Wine),
    path('boston/',views.Boston),
    path('cancer/',views.Cancer),
    path('irisgraphs/', views.Irisgraphs),
    path('winegraphs/', views.Winegraphs),
    path('bostongraphs/', views.Bostongraphs),
    path('cancergraphs/', views.Cancergraphs),
    path('irisgraphs/irisbar',views.irisBar),
    path('irisgraphs/irisscatter',views.irisScatter),
    path('irisgraphs/irishistogram', views.irisHistogram),
    path('irisgraphs/irispiechart', views.irisPiechart),
    path('irisgraphs/irisheatmap', views.irisHeatmap),
    path('irisgraphs/irisboxplot', views.irisBoxplot),
    path('bostongraphs/bostonscatter', views.bostonScatter),
    path('bostongraphs/bostonhistogram', views.bostonHistogram),
    path('bostongraphs/bostonheatmap', views.bostonHeatmap),
    path('bostongraphs/bostonboxplot', views.bostonBoxplot),
    path('winegraphs/winescatter', views.wineScatter),
    path('winegraphs/winehistogram', views.wineHistogram),
    path('winegraphs/wineheatmap', views.wineHeatmap),
    path('winegraphs/wineboxplot', views.wineBoxplot),
    path('winegraphs/winebar', views.wineBar),
    path('cancergraphs/cancerscatter', views.cancerScatter),
    path('cancergraphs/cancerhistogram', views.cancerHistogram),
    path('cancergraphs/cancerheatmap', views.cancerHeatmap),
    path('cancergraphs/cancerboxplot', views.cancerBoxplot),
    path('cancergraphs/cancerbar', views.cancerBar),



]
