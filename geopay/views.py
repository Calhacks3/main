from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = 'geopay/home.html'

    def get(self, request):
        """Returns the home page"""
        return render(request, self.template_name)
