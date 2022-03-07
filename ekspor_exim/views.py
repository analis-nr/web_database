from django.views.generic import ListView

from .models import Dataekspor

class EksporEximListView(ListView):
    model = Dataekspor
    template_name = 'ekspor_exim.html'
