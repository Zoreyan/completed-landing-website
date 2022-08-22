from calendar import prmonth
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import *
from .models import *
# Create your views here.


class HomeView(FormView):
    template_name = 'main/index.html'
    form_class = SubscribersForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        send_mail(f'Hello {form.cleaned_data["name"]}', 'You have been subscribed to e-mail receivment, you will be notified when site launch', 'your gmail "man@example.com"', [form.cleaned_data['email']])
        form.save()
        return super(HomeView, self).form_valid(form)