
from django.conf.urls import url
from interview import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
