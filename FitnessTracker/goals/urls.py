from django.urls import path, include

from FitnessTracker.goals.views import SetGoalView, GoalEditView, GoalDeleteView, approve_goal

urlpatterns = [
    path('set-goal/', SetGoalView.as_view(), name='set-goal'),
    path('<int:pk>/', include([
        path('approve/', approve_goal, name='approve'),
        path('edit-goal/', GoalEditView.as_view(), name='edit-goal'),
        path('delete-goal/', GoalDeleteView.as_view(), name='delete-goal'),
    ]))
]
