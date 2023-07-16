from django.urls import path
from .views import ThingListView,ThingDetailView,HomeView

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('thing/', ThingListView.as_view(),name='list'),
    path('thing/<pk>/',ThingDetailView.as_view(),name='details'),
]