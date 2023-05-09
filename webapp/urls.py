from . import views
from django.urls import path

# this is needed for class based views as an include in the core app

# in the index.html there is a control statement {% url 'post_detail' post.slug %}
# NOTE that the post_detail matches the name= value for the slug path converter <slug:slug> <pathconverter:keyword> below

urlpatterns = [
    path('', views.PilotList.as_view(), name='home')
]