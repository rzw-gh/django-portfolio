from django.shortcuts import render, get_object_or_404
from .models import Job

def home(request):
	job_list = Job.objects.all()
	return render(request, 'jobs/home.html', {'jobs':job_list})

def detail(request, job_id):
	job_detail = get_object_or_404(Job, pk=job_id)  #first_argument-->name of our model  second_argument-->every model in the database have primary key (pk)
	return render(request, 'jobs/detail.html', {'job':job_detail})