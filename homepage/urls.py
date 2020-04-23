from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'homepage'

urlpatterns = [
    # path('', views.IndexPageView.as_view()),

    path('sysadmin/', views.Sysadmin.as_view(), name='sysadmin'),
    path('developer/', views.Developer.as_view(), name='developer'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    url(r'^$', views.index, name='index'),
]


