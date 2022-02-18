from django.urls import path

from .views import ImporEximPageView

urlpatterns = [
    path('impor-exim/', ImporEximPageView.as_view(), name='impor_exim'),
]