from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def user_details(request):
    username = request.user.username
    user = User.objects.get(email=username)
    return render(request, 'user_details.html', {'user': user})