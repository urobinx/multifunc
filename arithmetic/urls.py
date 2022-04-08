from arithmetic import views
from django.urls import re_path


urlpatterns = [
    re_path(r'^t.+sum/', views.FigureUp.as_view()),
    re_path(r'^primes/', views.CountPrimes.as_view()),
]
