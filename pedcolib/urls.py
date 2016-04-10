"""pedcolib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^persons/', include('teachers.urls', namespace='persons')),
    url(r'^graduates/', include('graduates.urls', namespace='graduates')),
    url(r'^groups/', include('groups.urls', namespace='groups')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^responses/', include('responses.urls', namespace='responses')),
    url(r'^publications/', include('publications.urls', namespace='publications')),
    url(r'^gallery/', include('fvgallery.urls', namespace='gallery')),
    url(r'^captcha/', include('captcha.urls')),
    #url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^', include('home.urls', namespace='home')),
]