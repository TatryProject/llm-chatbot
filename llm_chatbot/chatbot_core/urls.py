from django.urls import path
from . import views

urlpatterns = [
    path("prompt-engineering", views.prompt_engineering, name="prompt_engineering"),
    path("prompt-engineering/status/<uuid:task_id>", views.get_prompt_engineering_status, name="get_prompt_engineering_status")
]