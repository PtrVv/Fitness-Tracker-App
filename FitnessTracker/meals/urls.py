from django.urls import path, include

from FitnessTracker.meals.views import MealsHomepage, AddMealView, EditMealView

urlpatterns = [
    path('', MealsHomepage.as_view(), name='meals-homepage'),
    path('add-meal/', AddMealView.as_view(), name='add-meal'),
    path('<int:pk>/', include([
        path('edit-meal/', EditMealView.as_view(), name='edit-meal'),
    ]))
]
