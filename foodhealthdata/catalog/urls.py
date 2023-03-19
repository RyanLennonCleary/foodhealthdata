from django.urls import path
from . import views, urls
from django.urls import include


urlpatterns = [
    path('', views.index, name='index'),
    path('foods/', views.FoodListView.as_view(), name='foods'),
    path('foods/<int:pk>/', views.FoodDetailView.as_view(), name='food-detail'),
    path('myfoods/',views.FoodsEatenByUser.as_view(), name='my-eaten'),
    path('signup/',views.Signup.as_view(), name='signup-user'),
    path('planner/', views.Planner.as_view(), name='planner'),
]
