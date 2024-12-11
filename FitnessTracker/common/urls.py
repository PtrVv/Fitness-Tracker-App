from django.urls import path
from FitnessTracker.common.views import PublicHomepageView, PrivateHomepageView, AboutPageView, PublicMealPlansView

urlpatterns = [
    path('', PublicHomepageView.as_view(), name='public-index'),
    path('goals/', PrivateHomepageView.as_view(), name='private-index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('about/shared-mealplans/', PublicMealPlansView.as_view(), name='shared-mealplans'),
]
