from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User as my_user

# Create your views here.
# Create your views here.
class Home(LoginRequiredMixin, View):
    login_url = '/login'
    # @decorators.login_required()
    def get(self, request):
        return render(request, 'home.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('login')

        login(request, user)
        return redirect('/')

        
class Register(View):
    def get(self, request):
        return render(request, 'register.html')
        

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email    = request.POST.get('email')
        team_id  = request.POST.get('team_id')
        user = my_user.objects.create_user(username=username,
                                         password=password,
                                         email=email,
                                         team_id=team_id)
        user.save()
        return HttpResponse('hihi')