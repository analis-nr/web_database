from django.urls import path

from .views import EksporEximPageView

urlpatterns = [
    path('ekspor-exim/', EksporEximPageView.as_view(), name='ekspor_exim'),
]