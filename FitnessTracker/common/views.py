from django.views.generic import TemplateView, ListView

from FitnessTracker.goals.models import Goal


class PrivateHomepageView(TemplateView):
    template_name = 'common/private-homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class PublicHomepageView(ListView):
    model = Goal
    context_object_name = 'goals'
    template_name = 'common/public-homepage.html'

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'goals.can_approve_goals' not in self.request.user.get_group_permissions() or not self.request.user.has_perm(
                'goals.can_approve_goals'):
            queryset = queryset.filter(approved=True)

        queryset = queryset.order_by('approved', '-created_at')

        return queryset
