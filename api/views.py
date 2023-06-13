from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, serializers

from core.models import Cards, Comments


class LoginAPIView(APIView):

    def post(self, *args, **kwargs):
        username = self.request.data.get('username')
        password = self.request.data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return Response(data='Вы вошли', status=status.HTTP_200_OK)
        return Response(data='Зарегистрируйся', status=status.HTTP_410_GONE)


class CreateTaskAPIView(APIView):

    def post(self, *args, **kwargs):
        title = self.request.data.get('title')
        description = self.request.data.get('description')
        performers = self.request.data.get('performers')
        deadline = self.request.data.get('deadline')
        c = Cards.objects.create(title=title, description=description,
                                deadline=deadline)
        for i in performers:
            c.performers.add(i)
        return Response(data='Успешно', status=status.HTTP_200_OK)


class CommentListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """Получаем все коментарии к карточке"""
        comment = Comments.objects.filter(card_id=kwargs['card_pk'])
        serializer = CommentListSerializers(instance=comment, many=True,
                                            context={"request": request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """Оставляем коментарий к карточке"""
        serializer = CommentCreateUpdateSerializers(
            data=request.data,
            context={"request": request})
        if serializer.is_valid():
            comment = Comments.objects.create(
                author_id=request.user.pk,
                text=serializer.data['text'],
                card_id=kwargs['card_pk']
            )
            serializer2 = CommentListSerializers(
                instance=comment,
                context={"request": request})
            return Response(serializer2.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['id', 'text', 'author']


class CommentCreateUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['text']