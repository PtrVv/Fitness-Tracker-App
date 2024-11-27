from django.urls import path, include

from FitnessTracker.workouts.views import WorkoutHomepage, AddWorkoutView, EditWorkoutView

urlpatterns = [
    path('', WorkoutHomepage.as_view(), name='workouts-homepage'),
    path('add-workout/', AddWorkoutView.as_view(), name='add-workout'),
    path('<int:pk>/', include([
        path('edit-workout/', EditWorkoutView.as_view(), name='edit-workout'),
    ]))
]
