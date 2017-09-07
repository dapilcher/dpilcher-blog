from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Post


class BlogHomeView(TemplateView):
    def get(self, request, **kwargs):
        latest_posts = Post.objects.order_by('-pub_date')[:5]
        context = {'latest_posts': latest_posts}
        return render(request, 'blog/home.html', context=context)


class DetailView(TemplateView):
    def get(self, request, post_id, **kwargs):
        latest_posts = Post.objects.order_by('-pub_date')[:5]
        post = get_object_or_404(Post, id=post_id)
        context = {'post': post,
                   'latest_posts': latest_posts}
        return render(request, 'blog/detail.html', context=context)


class YearArchiveView(TemplateView):
    def get(self, request, post_id, **kwargs):
        return render(request, 'blog/year_archive.html', context=None)
