from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import *
from .models import *
# Create your views here.


class HomeView(FormView):
    template_name = 'main/index.html'
    form_class = SubscribersForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form = form.save()
        return super(HomeView, self).form_valid(form)