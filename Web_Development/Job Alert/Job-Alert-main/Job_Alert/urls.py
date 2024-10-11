from django.urls import path
from . import views


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('set_profile', views.compulsary_profile.as_view(), name='compulsary-profile'),
    path('my_profile', views.my_profile.as_view(), name='my-profile'),
    path('edit_profile', views.edit_profile.as_view(), name='edit-profile')
]