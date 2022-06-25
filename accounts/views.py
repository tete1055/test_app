from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.

class SignUpView(CreateView):
    '''
    '''
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        '''
        parameters:
          from(django.forms.Form)
        Return:
        '''
        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    '''
    '''
    template_name = "signup_success.html"

