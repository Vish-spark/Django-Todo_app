from django.urls import path, include
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView
from django_prometheus import exports

urlpatterns = [
    path('', TaskList.as_view(),name='Tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(),name='task'),
    path('task-create/', TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(),name='task-delete'),
    path('', include('django_prometheus.urls')),
     path("metrics", exports.ExportToDjangoView, name="prometheus-django-metrics")

]