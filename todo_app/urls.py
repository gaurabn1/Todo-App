from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, logout_page, RegisterPage
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create_task/', TaskCreate.as_view(), name='create_task'),
    path('update_task/<int:pk>/', TaskUpdate.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', TaskDelete.as_view(), name='delete_task'),
    
    
    #logout
    path('logout/', logout_page, name='logout' ),
]