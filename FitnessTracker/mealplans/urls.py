from django.urls import path, include

from FitnessTracker.mealplans.views import MealPlanHomePageView, CreateMealPlanView, DeleteMealPlanView, \
    EditMealPlanView, DetailsMealPlanView

urlpatterns = [
    path('', MealPlanHomePageView.as_view(), name='mealplans-home'),
    path('add-mealplan/', CreateMealPlanView.as_view(), name='add-mealplan'),
    path('<int:pk>/', include([
        path('edit-mealplan/', EditMealPlanView.as_view(), name='edit-mealplan'),
        path('delete-mealplan/', DeleteMealPlanView.as_view(), name='delete-mealplan'),
        path('mealplan-details/', DetailsMealPlanView.as_view(), name='mealplan-details'),
    ]))
]
