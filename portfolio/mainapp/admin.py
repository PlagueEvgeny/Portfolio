from django.contrib import admin
from mainapp.models import Hello, About, Portfolio, Image, Certificate, Facts, Tools, UseTools

admin.site.register([Hello, About, Portfolio, Image, Certificate, Facts, Tools, UseTools])