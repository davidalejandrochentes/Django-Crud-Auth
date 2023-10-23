from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks_completed/', views.tasks_completed, name="tasks_completed"),
    path("tasks/create", views.create_tasks, name="create_task"),
    path('delete/<int:id>', views.delete_tasks, name="delete_tasks"),
    path('view/<int:id>', views.view_tasks, name="view_tasks"),
    path('view/<int:id>/completed', views.completed_tasks, name="completed_tasks"),
    path('edit/<int:id>', views.edit_tasks, name="edit_tasks"),
    path('login/', views.log_in, name="login"),
    path('singup/', views.sign_up, name="singup"),
    path('logout/', views.log_out, name="logout"),  
]
