from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .tasks import run_prompt_engineering
import django_rq
from rq.job import Job

def prompt_engineering(request):
    task = django_rq.enqueue(run_prompt_engineering)
    return JsonResponse({'task_id': task.id})

def get_prompt_engineering_status(request, task_id):
    task = Job.fetch(str(task_id), django_rq.get_connection())
    if task is None:
        return JsonResponse({'error': 'A job with this ID does not exist.'})
    
    if task.is_finished:
        return JsonResponse({'status': 'completed'})

    return JsonResponse({'status': 'pending'})