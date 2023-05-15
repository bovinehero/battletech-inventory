from . import views
from django.urls import path

# this is needed for class based views as an include in the core app

# in the index.html there is a control statement {% url 'post_detail' post.slug %}
# NOTE that the post_detail matches the name= value for the slug path converter <slug:slug> <pathconverter:keyword> below

urlpatterns = [
    path('', views.ActiveMechList.as_view(), name='home'),
    path('pilots/', views.PilotList.as_view(), name='pilots'),
    path('pilots/<slug:slug>', views.PilotDetail.as_view(), name='pilot_detail'),
    path('pilots/create/', views.CreatePilotView.as_view(), name="pilot_create"),
    path('pilots/<slug:slug>/update/', views.UpdatePilotView.as_view(), name="pilot_update"),
    path('pilots/<slug:slug>/delete/', views.DeletePilotView.as_view(), name="pilot_delete"),
    path('mechs/', views.MechList.as_view(), name='mechs'),
    path('mechs/create/', views.CreateMechView.as_view(), name="mech_create"),
    path('mechs/<slug:slug>/update/', views.UpdateMechView.as_view(), name="mech_update"),
    path('mechs/<slug:slug>/delete/', views.DeleteMechView.as_view(), name="mech_delete"),
    path('mechs/<slug:slug>', views.MechDetail.as_view(), name='mech_detail'),
    path('<slug:slug>', views.ActiveMechDetail.as_view(), name='active_mech_detail')
]