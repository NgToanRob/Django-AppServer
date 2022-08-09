from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Create your views here.
def index():
    pass


class Storage(LoginRequiredMixin, View):
    def post(self, request):
        pass
