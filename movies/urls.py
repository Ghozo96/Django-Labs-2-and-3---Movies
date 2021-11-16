from django.urls import path
from .views import create, details, movies_list, update, delete, register, login, logout

urlpatterns = [

    path('', movies_list, name='movies_list'),
    path('create', create, name='create'),
    path('details/<int:id>', details, name='details'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>/<str:name>', delete, name='delete'),

    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),

]