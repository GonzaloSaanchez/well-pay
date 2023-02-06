from django.shortcuts import render
from .models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def user_by_id(request, id):
    user = User.objects.get(user_id=id)
    return render(request, 'user_details.html', {'user': user})