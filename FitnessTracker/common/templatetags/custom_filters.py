from django import template

register = template.Library()


@register.filter
def join_names(queryset, delimiter=", "):
    return delimiter.join([item.name for item in queryset])
