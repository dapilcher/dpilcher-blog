from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='main_home'),
]