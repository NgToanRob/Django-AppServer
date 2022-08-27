from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User

# Create your views here.
# Create your views here.
class Home(LoginRequiredMixin, View):
    login_url = '/login'
    # @decorators.login_required()
    def get(self, request):
        return render(request, 'Account/home.html')


class Login(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'Account/login.html')
        return redirect('home')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('login')

        login(request, user)
        return redirect('/')

        
class Logout(View):
    def post(self, request):
        logout(request)
        return redirect('home')


class Register(View):
    def get(self, request):
        return render(request, 'Account/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email    = request.POST.get('email')
        team_id  = request.POST.get('team_id')

        user = User.objects.create_user(username=username,
                                         password=password,
                                         email=email,
                                         team_id=team_id)
        user.save()
        return redirect('login')