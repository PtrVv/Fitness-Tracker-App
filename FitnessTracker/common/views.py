from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'common/base.html'

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/private-homepage.html']
        else:
            return ['common/public-homepage.html']
