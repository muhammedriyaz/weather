from django.conf.urls import url
from frontend import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view()),
    url(r'^about/$',views.AboutPageView.as_view()),
    url('getWeatherData', views.getWeatherData)
]