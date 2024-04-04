from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .redis_utils import redis_conn, rq
from .tasks import run_prompt_engineering

def prompt_engineering(request):
    task = rq.enqueue(run_prompt_engineering)
    return JsonResponse({'task_id': task.id})

def get_prompt_engineering_status(request, task_id):
    print(str(task_id))
    task = rq.fetch_job(str(task_id))
    if task is None:
        return JsonResponse({'error': 'A job with this ID does not exist.'})
    
    if task.is_finished:
        return JsonResponse({'status': 'completed'})

    return JsonResponse({'status': 'pending'})