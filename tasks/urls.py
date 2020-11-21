from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = "List"),
	path('update_task/<str:taskId>/', views.updateTask, name = "update_task")
]