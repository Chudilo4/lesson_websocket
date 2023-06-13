from django.views.generic import TemplateView
from .models import MyUser, Cards

from sesame.utils import get_token
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {
            'title': 'Домашняя',
        }
        return context


class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = {
            'title': 'Авторизация',
        }
        return context


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = {
            'performers': MyUser.objects.all()
        }
        return context


class TaskListView(TemplateView):
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'cards': Cards.objects.all()
        }
        return context


class TaskDetailView(TemplateView):
    template_name = 'card_detail.html'

    def get_context_data(self, **kwargs):
        user = MyUser.objects.get(username=self.request.user.username)
        token = get_token(user)
        context = {
            'token': token
        }
        return context