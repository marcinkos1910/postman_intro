from django.urls import path

from home import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('next/', views.next_view, name='next_view'),
    path('detail/<int:pk>', views.detail_view, name='detail_view'),
    path('create', views.create_view, name='create_view'),
]