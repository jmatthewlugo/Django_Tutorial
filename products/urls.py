from django.urls import path
from . import views


# Note the index function isn't called
# This is because Django calls functions 
# at runtime

urlpatterns = [
    path('',views.index),
    path('new',views.new)
]