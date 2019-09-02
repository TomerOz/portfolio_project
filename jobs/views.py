from django.shortcuts import render

from .models import Job # importing the Job class


def home(request):
	jobs = Job.objects
	return render(request, 'jobs/home.html', {'jobs':jobs})
