from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from mainapp.models import Hello, About, Portfolio, Certificate, Tools


class HelloListView(ListView):
    model = Hello

class AboutListView(ListView):
    model = About

class PortfolioListView(ListView):
    model = Portfolio

    def get_queryset(self):
        if "search" in self.request.GET:
            search_title = self.request.GET["search"]
            queryset = Portfolio.objects.all()
            return queryset.filter(name__icontains=search_title)
        else:
            queryset = Portfolio.objects.all()
        return queryset

class CertificateListView(ListView):
    model = Certificate

class ToolsListView(ListView):
    model = Tools

class PortfolioDetailView(DetailView):
    model = Portfolio
