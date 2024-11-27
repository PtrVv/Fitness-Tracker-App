from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from FitnessTracker.workouts.forms import AddWorkoutForm, EditWorkoutForm
from FitnessTracker.workouts.models import Workout


class WorkoutHomepage(ListView):
    model = Workout
    template_name = 'workouts/workouts-homepage.html'
    context_object_name = 'workouts'
    paginate_by = 3

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)


class AddWorkoutView(CreateView):
    model = Workout
    form_class = AddWorkoutForm
    template_name = 'workouts/add-workout.html'
    success_url = reverse_lazy('workouts-homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditWorkoutView(UpdateView):
    model = Workout
    form_class = EditWorkoutForm
    template_name = 'workouts/edit-workout.html'
    success_url = reverse_lazy('workouts-homepage')
