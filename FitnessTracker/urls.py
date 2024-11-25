from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FitnessTracker.common.urls')),
    path('accounts/', include('FitnessTracker.accounts.urls')),
    path('goals/', include('FitnessTracker.goals.urls')),
    path('meals/', include('FitnessTracker.meals.urls')),
]
