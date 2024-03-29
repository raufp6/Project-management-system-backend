from django.urls import path,include
from . import views


from .views import GroupViewSet,UserRegViewSet,UserRetrieveUpdateDestroyAPIView,EmployeeViewSet,EmployeeRetrieveUpdateDestroyAPIView,PasswordChangeView,MyChatUsers

urlpatterns = [
    path('',UserRegViewSet.as_view(),name='user'),
    path('employee/',EmployeeViewSet.as_view(),name='employee'),
    path('employee/<int:pk>/',EmployeeRetrieveUpdateDestroyAPIView.as_view(),name='employee'),
    path('employee/<int:pk>/update/',EmployeeRetrieveUpdateDestroyAPIView.as_view(),name='employee'),
    path('group/',GroupViewSet.as_view(),name='user-group'),
    path('create/',EmployeeViewSet.as_view(),name='create-user'),
    path('<int:pk>/',UserRetrieveUpdateDestroyAPIView.as_view(),name="user-detail"),
    path('<int:pk>/update/',UserRetrieveUpdateDestroyAPIView.as_view(),name="user-update"),
    path('<int:pk>/delete/',UserRetrieveUpdateDestroyAPIView.as_view(),name="user-delete"),
    path('count/', views.user_count, name='user_count'),
    path('password-change/',PasswordChangeView.as_view(),name='password-change'),
    path('my_chatusers/',MyChatUsers.as_view(),name='chat-users')
    

]

