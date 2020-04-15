from django.urls import path
from . import views


app_name = 'homepage_app'


urlpatterns = [
    # path('', views.IndexPageView.as_view()),
    path('', views.index),
]
