from django.views.generic import TemplateView

from FitnessTracker.goals.models import Goal


class IndexView(TemplateView):
    template_name = 'common/base.html'

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/private-homepage.html']
        else:
            return ['common/public-homepage.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = Goal.objects.all()

        return context
