from django.urls import path
from FitnessTracker.common.views import PublicHomepageView, PrivateHomepageView

urlpatterns = [
    path('', PublicHomepageView.as_view(), name='public-index'),
    path('goals/', PrivateHomepageView.as_view(), name='private-index'),
]
