from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post


# Create your views here.
class HomeView(TemplateView):
    def get(self, request, **kwargs):
        latest_posts = Post.objects.order_by('-pub_date')[:5]
        context = {'latest_posts': latest_posts}
        return render(request, 'home/home.html', context=context)


class AboutView(TemplateView):
    def get(self, request, **kwargs):
        latest_posts = Post.objects.order_by('-pub_date')[:5]
        context = {'latest_posts': latest_posts}
        return render(request, 'home/about.html', context=context)


class ContactView(TemplateView):
    def get(self, request, **kwargs):
        latest_posts = Post.objects.order_by('-pub_date')[:5]
        context = {'latest_posts': latest_posts}
        return render(request, 'home/contact.html', context=context)
