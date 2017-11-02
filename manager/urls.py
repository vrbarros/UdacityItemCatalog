"""itemcatalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^items/add/$', views.items_add, name='items_add'),
    url(r'^items/edit/(?P<id>[\w-]+)/$',
        views.items_edit, name='items_edit'),
    url(r'^items/delete/(?P<id>[\w-]+)/$',
        views.items_delete, name='items_delete'),
    # This URL's needed to be at the end of the array to avoid confusion with CRUD
    url(r'^items/(?P<view>[\w-]+)/$', views.items, name='items'),
    url(r'^items/(?P<view>[\w-]+)/(?P<category>[\w-]+)/$',
        views.items, name='items_category'),
    url(r'^items/(?P<view>[\w-]+)/(?P<category>[\w-]+)/(?P<item>[\w-]+)/$',
        views.items, name='items_item'),

]
