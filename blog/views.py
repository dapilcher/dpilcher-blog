from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'blog/index.html', context=None)