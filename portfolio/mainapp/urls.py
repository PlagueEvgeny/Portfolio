import mainapp.views as mainapp
from django.urls import path
from mainapp.views import HelloListView, AboutListView, PortfolioListView, CertificateListView, PortfolioDetailView, ToolsListView

app_name = 'mainapp'

urlpatterns = [
    path('', HelloListView.as_view(), name='hello'),
    path('about', AboutListView.as_view(), name='about'),
    path('tools', ToolsListView.as_view(), name='tools'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio'),
    path('certificate/', CertificateListView.as_view(), name='certificate'),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_section'),
]