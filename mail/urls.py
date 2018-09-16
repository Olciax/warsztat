"""warsztat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import url

app_name = 'mail'


urlpatterns = [


    path('', views.view, name="index"),
    path('admin/', admin.site.urls),
    path('<int:person_id>/', views.details, name="details"),
    path('edit/<int:person_id>', views.edit, name="edit"),
    path('add/', views.PersonCreate.as_view(), name='person-add'),
    url(r'person/(?P<pk>[0-9]+)/$', views.PersonUpdate.as_view(), name='person-update'),
    url(r'person/(?P<pk>[0-9]+)/delete/$', views.PersonDelete.as_view(), name='person-delete')
]
