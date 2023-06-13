from django.contrib import admin
from .models import MyUser, Cards, Comments
# Register your models here.


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass