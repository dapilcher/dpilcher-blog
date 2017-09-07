from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.BlogHomeView.as_view(), name='blog_home'),
    url(r'^(?P<post_id>[0-9]+)/$', views.DetailView.as_view(), name='blog_detail'),
]