from django.urls import path
from . import views

app_name = "Dwitter"

urlpatterns = [
    path('',views.homeview, name="homepage"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('profile_list/', views.profile_list, name = 'profile_list'),
    path('profile/<int:pk>', views.profile, name = 'profile'),
]