from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Post


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        latest_posts = Post.objects.order_by('-pub_date')[:2]
        context = {'latest_posts':latest_posts}
        return render(request, 'blog/index.html', context=context)
