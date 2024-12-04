from django.urls import path

from FitnessTracker.program.views import AddWeekDayView, WeekDayHomepage, WeekDayDetailsView

urlpatterns = [
    path('', WeekDayHomepage.as_view(), name='program-home'),
    path('add-weekday/', AddWeekDayView.as_view(), name='add-weekday'),
    path('<str:weekday>/details/', WeekDayDetailsView.as_view(), name='edit-weekday'),
]
