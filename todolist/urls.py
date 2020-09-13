
from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),
    path('completed/<todo_id>', views.completedTodo, name='completed'),
    path('deleteCompleted', views.deleteCompleted, name='deleteCompleted'),
    path('deleteAll',views.deleteAll,name='deleteAll')

]
