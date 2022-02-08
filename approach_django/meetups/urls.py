from django.urls import path
from . import views
# django will be looking for the following line URLPATTERNS(in lowercase)
# here is where you add the views that are require
urlpatterns = [
    path('', views.index, name='all-meetups'), # the 'name' attribute is use to specify the url
    path('<slug:meetup_slug>/registration_success/', views.registration_success, name='registration_success'), 
    path('<slug:meetup_slug>/', views.more_details, name='meetup-detail'),
]