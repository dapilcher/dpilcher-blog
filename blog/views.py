from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Post


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        latest_posts = Post.objects.order_by('-pub_date')[:5]
        context = {'latest_posts': latest_posts}
        return render(request, 'blog/home.html', context=context)


class DetailView(TemplateView):
    def get(self, request, post_id, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        context = {'post': post}
        return render(request, 'blog/detail.html', context=context)
