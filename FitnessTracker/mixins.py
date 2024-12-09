from django import forms
from django.http import Http404


class DisableFieldsMixin(forms.Form):
    disabled_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.disabled_fields[0] == '__all__' or field_name in self.disabled_fields:
                field.disabled = True


class UserOwnershipMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        if obj.user != self.request.user:
            raise Http404("You are not authorized to access or modify this object.")

        return obj
