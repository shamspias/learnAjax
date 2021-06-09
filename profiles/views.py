from django.shortcuts import render
from .models import Profiles
from .forms import ProfileForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required
def my_profile_view(request):
    pass
