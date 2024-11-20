from django.urls import path
from FitnessTracker.common.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
