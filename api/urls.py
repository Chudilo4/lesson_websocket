from django.urls import path
from .views import LoginAPIView, CreateTaskAPIView, CommentListAPIView

urlpatterns = [
    path('sdflogin/', LoginAPIView.as_view(), name='avb'),
    path('task/', CreateTaskAPIView.as_view(), name='create_task'),
    path('task/<int:card_pk>/comment/', CommentListAPIView.as_view(),
         name='comment_list')
]
