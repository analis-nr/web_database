from django.views.generic import TemplateView

class HomePageView (TemplateView):
    template_name = 'home.html'

class ImporEximPageView (TemplateView):
    template_name = 'impor_exim.html'

class EksporEximPageView (TemplateView):
    template_name = 'ekspor_exim.html'
