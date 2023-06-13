from django.urls import path
from .views import HomeView, LoginView, TaskView, TaskDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='weq'),
    path('task/', TaskView.as_view(), name='task'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail')
]
