from django.urls import path

from .views import EksporEximListView

urlpatterns = [
    path('ekspor-exim/', EksporEximListView.as_view(), name='ekspor_exim'),
]