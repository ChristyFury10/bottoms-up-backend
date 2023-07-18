from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name = "routes"),
    path('bars/', views.getBars, name="bars"),
    path('bars/create', views.createBar, name="create-bar"),
    path('bars/<str:pk>/update', views.updateBar, name="update-bar"),
    path('bars/<str:pk>/', views.getBar, name="bar"),
    path('bars/<str:pk>/delete', views.deleteBar, name="delete-bar"),
    path('bars/<str:pk>/specials/new', views.createSpecial, name="special-create"),
    path('bars/<int:bar_pk>/specials/<int:special_pk>', views.viewSpecial, name="special-view"),
    path('bars/<int:bar_pk>/specials/<int:special_pk>/update', views.updateSpecial, name="special-update"),
    path('bars/<int:bar_pk>/specials/<int:special_pk>/delete', views.deleteSpecial, name="delete-special"),




    
    



]