from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('robokop/<int:dk>/', views.robokop, name='robokop'),
    #path('checkLIST2', views.checkLIST2, name='checkLIST2'),
    path('checkLIST2', views.Task_new2, name='checkLIST2'),
    path('change_status2/<int:i>/', views.change_status2, name='change_status2'),
    path('delete_all2', views.delete_all2, name='delete_all2'),
    path('delete_done2', views.delete_done2, name='delete_done2'),
    path('mark_all_as_done2', views.mark_all_as_done2, name='mark_all_as_done2'),

]